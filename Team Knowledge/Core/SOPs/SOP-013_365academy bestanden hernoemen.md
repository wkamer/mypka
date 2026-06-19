# SOP-013 — 365 Academy bestanden hernoemen

## Purpose

Repeatable procedure for renaming raw 365 Academy lesson files to a consistent, human-readable pattern per module. Covers title extraction, Windows-safe filename rules, and script invocation.

---

## Naming Pattern

```
Les <nr>. <title>.<ext>
```

Example:

```
Les 7. Je bent niet de golf; je bent de oceaan.mp4
```

- **`Les <nr>`** — take the lesson number from the source filename
- **Title** — extracted from `<h1>` in the corresponding `.txt` file (see below)
- **Extension** — `mp4`, `srt`, `txt`, `jpg` (all four file types per lesson)

> **Previous pattern** (pre-2026-05-25): `Module 1. Vrijheid - Les <nr>. <title>.<ext>` — stripped by the script via `OLD_PREFIX = "Module 1. Vrijheid - "`.

---

## Title Extraction Logic

1. Open the `.txt` file for the lesson (pattern: `365-academy - 1.<nr> <anything>.txt` for original source files, or the current `Les <nr>. <title>.txt` for already-renamed files)
2. Find the first `<h1>...</h1>` tag using regex: `<h1>(.*?)</h1>`
3. Strip any leading number prefix from the `<h1>` content: `^\d+\.\s*` (note: use `\s*` not `\s+` — some h1 values have no space after the period, e.g. `60.Alles is al vergeven`)
4. Strip any trailing period from the extracted title (some h1 values end with a period, e.g. `Je bent niet schuldig; je hebt je vergist.`)
5. Apply the semicolon rule (see below)
6. Use the resulting string as the title in the new filename

---

## Semicolon Rule (Windows Compatibility)

Colons (`:`) are forbidden in Windows filenames. Every colon found in an extracted `<h1>` title **must be replaced with a semicolon** (`;`) before building the new filename.

This replacement happens inside `extract_h1_title()` in the script:

```python
stripped = stripped.replace(":", ";")
```

This rule applies to all modules, not just Module 1.

---

## Script Location

```
Team Knowledge/Core/Scripts/rename_365academy_module1.py
```

When adding a new module, either:
- Extend the existing script with new constants and logic, or
- Create a new script `rename_365academy_module<N>.py` following the same structure

---

## Invoking the Script

**Preview (safe, no changes):**

```bash
python3 "Team Knowledge/Core/Scripts/rename_365academy_module1.py"
```

**Execute (performs actual renames):**

```bash
python3 "Team Knowledge/Core/Scripts/rename_365academy_module1.py" --execute
```

Always run in preview mode first and verify the mapping before running with `--execute`.

---

## Script Parameters

| Constant | Description |
|----------|-------------|
| `FOLDER` | Absolute path to the folder containing the lesson files |
| `OLD_PREFIX` | Prefix to strip from already-renamed files (e.g. `Module 1. Vrijheid - `) |
| `SKIP_FILE` | Filename to skip (intro file that does not follow the lesson pattern) |

No hardcoded logic for lesson numbers — the script derives them from filenames automatically.

---

## File Types Handled

| Extension | Source pattern | Match method |
|-----------|---------------|--------------|
| `.mp4` | `Module 1. Vrijheid - Les <nr>. <title>.mp4` (current) or `365-academy - 1.<nr> <title>.mp4` (original) | `current_re` / `media_re` |
| `.srt` | `Module 1. Vrijheid - Les <nr>. <title>.srt` (current) or `365-academy - 1.<nr> <title>.srt` (original) | `current_re` / `media_re` |
| `.txt` | `Module 1. Vrijheid - Les <nr>. <title>.txt` (current) or `365-academy - 1.<nr> <title>.txt` (original) | `current_re` / `media_re` |
| `.jpg` | `Module 1. Vrijheid - Les <nr>. <title>.jpg` (current) or `<timestamp>-miracle-roadmap_les-<nr>.jpg` (original) | `current_re` / `jpg_re` |

> **Edge case:** the separator before `les` in the jpg filename is inconsistent across modules. Most files use `_les-` (underscore) but some use `-les-` (hyphen), e.g. `215138-miracle-roadmap-les-47.jpg`. The `jpg_re` regex must use `[-_]les-` to match both variants.

---

## Expected Output

The script prints a preview table and, after `--execute`, confirms each rename. Final line: `Done. N files renamed.`

---

## Checklist Before Running

- [ ] Source folder path is correct in `FOLDER`
- [ ] All `.txt` files are present and contain a valid `<h1>` tag
- [ ] Preview output looks correct (titles extracted, no errors)
- [ ] Run with `--execute` only after preview approval

---

---

## Step 2 — Generate Markdown Files Per Lesson

After the rename step, run `create_365academy_md_files.py` to generate 3 Markdown files per lesson.

### Output per lesson

| File | Source | Method |
|------|--------|--------|
| `Les <nr>. <titel> - Transcript.md` | `.srt` file | Strip SRT sequence numbers and timestamps; join lines into running Dutch text |
| `Les <nr>. <titel> - Samenvatting.md` | Transcript text | Claude API (`claude-sonnet-4-6`) — structured summary in Dutch |
| `Les <nr>. <titel> - Opdracht.md` | `.txt` file (HTML) | `html2text` library — pure HTML-to-Markdown, no AI |

### Summary structure

```
# Les <nr>. <titel>

## Kernboodschap
<1-2 zinnen>

## Inzichten
- <inzicht 1>
- <inzicht 2>
- ...

## Quote
<één krachtige zin uit de les>
```

### Script location

```
Team Knowledge/Core/Scripts/create_365academy_md_files.py
```

### Invoking the script

```bash
python3 "Team Knowledge/Core/Scripts/create_365academy_md_files.py"
```

Optional: pass a custom folder path:

```bash
python3 "Team Knowledge/Core/Scripts/create_365academy_md_files.py" --folder "/opt/myPKA/Team Inbox/2. AndereModule"
```

### Requirements

- `ANTHROPIC_API_KEY` in environment, or set in `memory_config` (loaded automatically)
- Python packages: `anthropic`, `html2text` — install if missing: `pip3 install anthropic html2text`
- All `.srt` and `.txt` files must be present in the folder (already guaranteed after Step 1)

### Error handling

On any per-file API or IO error: writes a file with the error message and continues. The final summary shows counts per type and lists all errors.

---

---

## Step 3 — Generate PDFs Per Lesson

After Step 2, run `generate_365academy_pdfs.py` to generate one PDF per lesson.

### Output per lesson

| File | Contents | Layout |
|------|----------|--------|
| `Les <nr>. <titel>.pdf` | Samenvatting + page break + Opdracht | A4, 3 cm margins |

### Script location

```
Team Knowledge/Core/Scripts/generate_365academy_pdfs.py
```

### Invoking the script

```bash
python3 "Team Knowledge/Core/Scripts/generate_365academy_pdfs.py"
```

Optional: pass a custom folder path:

```bash
python3 "Team Knowledge/Core/Scripts/generate_365academy_pdfs.py" --folder "/opt/myPKA/Team Inbox/2. AndereModule"
```

### Engine detection (automatic)

| Priority | Engine | Condition |
|----------|--------|-----------|
| 1 | `xelatex` via pandoc | `pandoc` + `xelatex` both in PATH |
| 2 | `pdflatex` via pandoc | `pandoc` + `pdflatex` both in PATH |
| 3 | `reportlab` (pure Python) | Fallback — always available via venv |

No manual configuration needed. The script detects and uses the best available engine.

### Requirements

- Python package `reportlab` — install if missing: `pip3 install reportlab`
- Samenvatting and Opdracht `.md` files must be present (guaranteed after Step 2)
- Optional: DejaVu fonts at `/usr/share/fonts/truetype/dejavu/` — used automatically for full Unicode support

### Error handling

On any per-lesson error: prints the error and continues. Final summary shows counts and lists all errors.

---

## Step 4 — Verwerk het introductie-bestand

Elke module heeft één introductie `.txt` bestand (HTML). Dit wordt apart verwerkt naar MD en PDF.

### Naamgeving

- Bronbestand: `Introductie - <ondertitel>.txt`
- Puntkomma-regel: colons in de bestandsnaam vervangen door puntkomma's
- Output: `Introductie - <ondertitel>.md` en `Introductie - <ondertitel>.pdf`

### MD aanmaken

Converteer het `.txt` bronbestand (HTML) naar Markdown via `html2text` — zelfde logica als de Opdracht-bestanden in Step 2.

### PDF aanmaken

```bash
python3 "Team Knowledge/Core/Scripts/generate_365academy_pdfs.py" --intro --folder "/opt/myPKA/Team Inbox/<module folder>"
```

### PDF-layout intro

| Element | Opmaak |
|---------|--------|
| Label "INTRODUCTIE" | `style_label` — light_grey (#666666), 16pt, bovenaan |
| Titel (uit `<h1>`, zonder "Introductie - " prefix) | `style_title` — accent kleur, 18pt |
| Content | Zelfde body-stijl als les-PDFs |

- Puntkomma-regel ook op de `<h1>` titel toepassen vóór rendering
- "Introductie - " prefix strippen uit de `<h1>` zodat alleen het onderwerp als titel verschijnt
- Geen samenvatting/opdracht splitsing — één doorlopende pagina

### Volgorde intro-bestand hernoemen

1. Hernoem `.txt` bronbestand met puntkomma (indien van toepassing)
2. Genereer `.md` via html2text
3. Genereer `.pdf` via `--intro` flag

---

*Created: 2026-05-25 | Updated: 2026-05-28 | Owner: Kai*
