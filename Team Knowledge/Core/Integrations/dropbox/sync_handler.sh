#!/bin/bash
# Copies new audio from Dropbox to Team Inbox, then deletes from Dropbox.
# Sends a Team Inbox notification per file via the Discord integration.
# After copy: transcribes each .m4a via whisper and writes transcript to Team Inbox.
# Deletes .m4a only after successful transcription (exit code 0 from transcribe_handler).
#
# Also syncs WhatsApp exports from dropbox:/Whatsapp Export:
# Downloads each zip, unpacks _chat.txt, runs whatsapp_export_handler.py,
# deletes zip from Dropbox on success. Uses its own lockfile.

INTEGRATION_DIR="$(cd "$(dirname "$0")" && pwd)"
LOCKFILE=/tmp/dropbox-recorded-audio-sync.lock
LOGFILE="$INTEGRATION_DIR/logs/dropbox-recorded-audio-sync.log"
RCLONE_CONF="$INTEGRATION_DIR/rclone.conf"
NOTIFY="/opt/myPKA/Team Knowledge/Core/Integrations/discord/notify_team_inbox.sh"
TRANSCRIBE="/opt/myPKA/Team Knowledge/Core/Integrations/whisper/transcribe_handler.py"
WHISPER_PYTHON="/opt/whisper/venv/bin/python"
SOURCE="dropbox:/Team Inbox/Recorded Audio"
DEST="/opt/myPKA/Team Inbox/Recorded Audio"

if [ -f "$LOCKFILE" ]; then
    echo "$(date): sync already running, skipping" >> "$LOGFILE"
    exit 0
fi

touch "$LOCKFILE"
trap "rm -f $LOCKFILE" EXIT

# List files to be synced
files=$(rclone lsf "$SOURCE" --config="$RCLONE_CONF" 2>/dev/null)

# Copy new files to Team Inbox
rclone copy "$SOURCE" "$DEST" \
    --config="$RCLONE_CONF" \
    --no-update-modtime \
    --log-file="$LOGFILE" \
    --log-level INFO

if [ $? -eq 0 ]; then
    # Notify per file
    while IFS= read -r file; do
        [ -z "$file" ] && continue
        bash "$NOTIFY" "iPhone" "$DEST/$file"
    done <<< "$files"

    # Transcribe each .m4a file; delete only on success
    while IFS= read -r file; do
        [ -z "$file" ] && continue

        # Only transcribe audio files
        case "$file" in
            *.m4a|*.mp3|*.wav|*.ogg|*.flac)
                AUDIO_PATH="$DEST/$file"
                echo "$(date): transcribing $file" >> "$LOGFILE"

                "$WHISPER_PYTHON" "$TRANSCRIBE" "$AUDIO_PATH" >> "$LOGFILE" 2>&1
                EXIT_CODE=$?

                if [ $EXIT_CODE -eq 0 ]; then
                    echo "$(date): transcription OK — removing $file from Dropbox" >> "$LOGFILE"
                    rclone deletefile "$SOURCE/$file" \
                        --config="$RCLONE_CONF" \
                        --log-file="$LOGFILE" \
                        --log-level INFO
                    # Remove local copy after successful transcription
                    rm -f "$AUDIO_PATH"
                    echo "$(date): removed local copy $AUDIO_PATH" >> "$LOGFILE"
                else
                    echo "$(date): ERROR — transcription failed for $file (exit $EXIT_CODE) — keeping .m4a" >> "$LOGFILE"
                fi
                ;;
            *)
                # Non-audio file: skip transcription, still delete from Dropbox
                echo "$(date): non-audio file $file — skipping transcription" >> "$LOGFILE"
                rclone deletefile "$SOURCE/$file" \
                    --config="$RCLONE_CONF" \
                    --log-file="$LOGFILE" \
                    --log-level INFO
                ;;
        esac
    done <<< "$files"
fi

# ===========================================================================
# Team Inbox sync
# Copies files dropped in dropbox:/Team Inbox to /opt/myPKA/Team Inbox/.
# Notifies per file via notify_team_inbox.sh, then deletes from Dropbox.
# Own lockfile so this block runs independently of the audio block above.
# ===========================================================================
TI_LOCKFILE=/tmp/dropbox-team-inbox-sync.lock
TI_LOGFILE="$INTEGRATION_DIR/logs/dropbox-team-inbox-sync.log"
TI_SOURCE="dropbox:/Team Inbox"
TI_DEST="/opt/myPKA/Team Inbox"

if [ -f "$TI_LOCKFILE" ]; then
    echo "$(date): Team Inbox sync already running, skipping" >> "$TI_LOGFILE"
else
    touch "$TI_LOCKFILE"
    trap "rm -f $TI_LOCKFILE" EXIT

    # List files to be synced
    ti_files=$(rclone lsf "$TI_SOURCE" --files-only --config="$RCLONE_CONF" 2>/dev/null)

    # Copy files to Team Inbox root (flat, no subfolder)
    rclone copy "$TI_SOURCE" "$TI_DEST" \
        --config="$RCLONE_CONF" \
        --no-update-modtime \
        --max-depth 1 \
        --log-file="$TI_LOGFILE" \
        --log-level INFO

    if [ $? -eq 0 ]; then
        while IFS= read -r file; do
            [ -z "$file" ] && continue
            bash "$NOTIFY" "Team Inbox" "$TI_DEST/$file"
            rclone deletefile "$TI_SOURCE/$file" \
                --config="$RCLONE_CONF" \
                --log-file="$TI_LOGFILE" \
                --log-level INFO
        done <<< "$ti_files"
    fi

    rm -f "$TI_LOCKFILE"
fi

# ===========================================================================
# WhatsApp Export sync
# Own lockfile so this block runs independently of the audio block above.
# ===========================================================================
WA_LOCKFILE=/tmp/dropbox-whatsapp-export-sync.lock
WA_LOGFILE="$INTEGRATION_DIR/logs/whatsapp_export.log"
WA_SOURCE="dropbox:/Team Inbox/Whatsapp Export"
WA_HANDLER="$INTEGRATION_DIR/whatsapp_export_handler.py"
WA_PYTHON="/usr/bin/python3"
WA_TEMP="/tmp/mypka_wa_export"

if [ -f "$WA_LOCKFILE" ]; then
    echo "$(date): WhatsApp export sync already running, skipping" >> "$WA_LOGFILE"
    exit 0
fi

touch "$WA_LOCKFILE"
trap "rm -f $LOCKFILE; rm -f $WA_LOCKFILE; rm -rf $WA_TEMP" EXIT

# List zip files in Dropbox WhatsApp Export folder
wa_files=$(rclone lsf "$WA_SOURCE" --config="$RCLONE_CONF" 2>/dev/null)

if [ -z "$wa_files" ]; then
    echo "$(date): WhatsApp Export — no files found" >> "$WA_LOGFILE"
    exit 0
fi

mkdir -p "$WA_TEMP"

while IFS= read -r zip_file; do
    [ -z "$zip_file" ] && continue

    # Only process zip files
    case "$zip_file" in
        *.zip) ;;
        *)
            echo "$(date): WhatsApp Export — skipping non-zip file: $zip_file" >> "$WA_LOGFILE"
            continue
            ;;
    esac

    echo "$(date): WhatsApp Export — downloading $zip_file" >> "$WA_LOGFILE"

    # Unique temp dir per zip to avoid cross-contamination
    EXTRACT_DIR="$WA_TEMP/$(basename "$zip_file" .zip)"
    mkdir -p "$EXTRACT_DIR"

    # Download the zip to temp
    rclone copyto "$WA_SOURCE/$zip_file" "$EXTRACT_DIR/$zip_file" \
        --config="$RCLONE_CONF" \
        --log-file="$WA_LOGFILE" \
        --log-level INFO

    if [ $? -ne 0 ]; then
        echo "$(date): WhatsApp Export — ERROR downloading $zip_file — skipping" >> "$WA_LOGFILE"
        rm -rf "$EXTRACT_DIR"
        continue
    fi

    # Unzip
    unzip -q "$EXTRACT_DIR/$zip_file" -d "$EXTRACT_DIR" 2>> "$WA_LOGFILE"
    if [ $? -ne 0 ]; then
        echo "$(date): WhatsApp Export — ERROR unzipping $zip_file — skipping" >> "$WA_LOGFILE"
        rm -rf "$EXTRACT_DIR"
        continue
    fi

    # Locate _chat.txt (may be nested inside a subfolder)
    CHAT_FILE=$(find "$EXTRACT_DIR" -name "_chat.txt" | head -1)
    if [ -z "$CHAT_FILE" ]; then
        echo "$(date): WhatsApp Export — no _chat.txt found in $zip_file — skipping" >> "$WA_LOGFILE"
        rm -rf "$EXTRACT_DIR"
        continue
    fi

    echo "$(date): WhatsApp Export — processing $CHAT_FILE" >> "$WA_LOGFILE"

    # Save a copy of the raw _chat.txt for format inspection (overwritten each run)
    RAW_DEBUG_DIR="$INTEGRATION_DIR/logs"
    cp "$CHAT_FILE" "$RAW_DEBUG_DIR/_chat_debug_$(basename "$zip_file" .zip | tr ' ' '_').txt" 2>/dev/null

    # Derive chat slug from zip filename:
    # "WhatsApp Chat - Wendy Opdam.zip" -> "wendy-opdam"
    # Strip "WhatsApp Chat - " prefix and ".zip" suffix, lowercase, non-alphanumeric to "-", collapse runs
    CHAT_SLUG=$(echo "$zip_file" \
        | sed 's/^WhatsApp Chat - //' \
        | sed 's/\.zip$//' \
        | tr '[:upper:]' '[:lower:]' \
        | sed 's/[^a-z0-9]/-/g' \
        | sed 's/-\+/-/g' \
        | sed 's/^-//' \
        | sed 's/-$//')
    echo "$(date): WhatsApp Export — chat slug: $CHAT_SLUG" >> "$WA_LOGFILE"

    # Output dir: per-slug mapping to the correct project folder
    MYPKA_ROOT="$(cd "$INTEGRATION_DIR/../../../.." && pwd)"
    case "$CHAT_SLUG" in
        wendy-opdam)
            WA_OUTPUT_DIR="$MYPKA_ROOT/PKM/My Life/Projects/P-Scheiding/WhatsApp"
            ;;
        *)
            WA_OUTPUT_DIR="$MYPKA_ROOT/PKM/CRM/WhatsApp/$CHAT_SLUG"
            ;;
    esac

    # Capture stdout (written file paths) separately from log
    WA_WRITTEN=$("$WA_PYTHON" "$WA_HANDLER" "$CHAT_FILE" \
        --chat-slug "$CHAT_SLUG" \
        --from-date "${WA_FROM_DATE:-01/01/2026}" \
        --output-dir "$WA_OUTPUT_DIR" \
        2>> "$WA_LOGFILE")
    WA_EXIT=$?

    if [ $WA_EXIT -eq 0 ]; then
        echo "$(date): WhatsApp Export — handler OK — deleting $zip_file from Dropbox" >> "$WA_LOGFILE"
        rclone deletefile "$WA_SOURCE/$zip_file" \
            --config="$RCLONE_CONF" \
            --log-file="$WA_LOGFILE" \
            --log-level INFO

        # Count new days written and send ONE summary notification
        WA_COUNT=$(echo "$WA_WRITTEN" | grep -c "\.md$" || echo 0)
        if [ "$WA_COUNT" -gt 0 ]; then
            bash "$NOTIFY" "WhatsApp Export" "$WA_COUNT nieuwe dag(en) verwerkt voor $CHAT_SLUG → $WA_OUTPUT_DIR"
        else
            echo "$(date): WhatsApp Export — geen nieuwe berichten — geen notificatie verstuurd" >> "$WA_LOGFILE"
        fi
    else
        echo "$(date): WhatsApp Export — ERROR — handler failed for $zip_file (exit $WA_EXIT) — keeping zip in Dropbox" >> "$WA_LOGFILE"
    fi

    rm -rf "$EXTRACT_DIR"

done <<< "$wa_files"
