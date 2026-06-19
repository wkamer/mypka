#!/usr/bin/env python3
"""
generate_365academy_pdfs.py

Generates one PDF per lesson combining:
  1. Samenvatting (summary)
  2. Page break
  3. Opdracht (assignment)

Also generates a single-page intro PDF from an intro Markdown file.

Output: Les <nr>. <titel>.pdf (lessons) or <naam>.pdf (intro) in the source folder.

Engine: ReportLab (pure Python, no system LaTeX required)
Fallback detection: checks for pandoc+xelatex, pandoc+pdflatex, then uses ReportLab.

Usage:
    /opt/mypka-memory/venv/bin/python generate_365academy_pdfs.py [--folder PATH]
    /opt/mypka-memory/venv/bin/python generate_365academy_pdfs.py --intro [--folder PATH]
"""

import argparse
import glob
import os
import re
import subprocess
import sys
import tempfile

try:
    from PIL import Image as PILImage
    _PIL_AVAILABLE = True
except ImportError:
    _PIL_AVAILABLE = False

DEFAULT_FOLDER = "/opt/myPKA/Team Inbox/1. Vrijheid"


def detect_engine():
    """Return best available PDF engine: 'xelatex', 'pdflatex', or 'reportlab'."""
    pandoc = subprocess.run(["which", "pandoc"], capture_output=True).returncode == 0
    if pandoc:
        if subprocess.run(["which", "xelatex"], capture_output=True).returncode == 0:
            return "xelatex"
        if subprocess.run(["which", "pdflatex"], capture_output=True).returncode == 0:
            return "pdflatex"
    return "reportlab"


def find_lessons(folder):
    """Return sorted list of (nr, title) tuples for all lessons that have both md files."""
    pattern = os.path.join(folder, "Les *.* - Samenvatting.md")
    sam_files = glob.glob(pattern)
    lessons = []
    for sam_path in sam_files:
        basename = os.path.basename(sam_path)
        # Extract "Les <nr>. <titel>" from "Les <nr>. <titel> - Samenvatting.md"
        m = re.match(r"^(Les (\d+)\..+?) - Samenvatting\.md$", basename)
        if not m:
            continue
        lesson_name = m.group(1)  # e.g. "Les 7. Je bent niet de golf; je bent de oceaan"
        nr = int(m.group(2))
        opdracht_path = os.path.join(folder, lesson_name + " - Opdracht.md")
        if not os.path.exists(opdracht_path):
            print(f"  WARNING: No Opdracht file for {lesson_name} — skipping")
            continue
        lessons.append((nr, lesson_name, sam_path, opdracht_path))
    lessons.sort(key=lambda x: x[0])
    return lessons


def read_md(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def strip_html_tags(text):
    """Remove HTML tags and convert common HTML entities to plain text."""
    # Convert common bold/italic tags to markdown equivalents before stripping
    text = re.sub(r"<b>(.*?)</b>", r"**\1**", text, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r"<strong>(.*?)</strong>", r"**\1**", text, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r"<i>(.*?)</i>", r"*\1*", text, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r"<em>(.*?)</em>", r"*\1*", text, flags=re.IGNORECASE | re.DOTALL)
    # Strip remaining HTML tags
    text = re.sub(r"<[^>]+>", "", text)
    # Decode common HTML entities
    text = text.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")
    text = text.replace("&nbsp;", " ").replace("&quot;", '"').replace("&#39;", "'")
    return text


# ---------------------------------------------------------------------------
# ReportLab renderer
# ---------------------------------------------------------------------------

def generate_pdf_reportlab(lesson_name, samenvatting_text, opdracht_text, output_path):
    """Generate a single-lesson PDF using ReportLab."""
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import cm
    from reportlab.lib.colors import HexColor
    from reportlab.lib.enums import TA_LEFT
    from reportlab.platypus import (
        SimpleDocTemplate, Paragraph, Spacer, PageBreak, HRFlowable,
    )
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont

    # Use a Unicode-capable font if available (DejaVu), otherwise Helvetica
    font_regular = "Helvetica"
    font_bold = "Helvetica-Bold"
    try:
        dejavu_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
        dejavu_bold_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
        if os.path.exists(dejavu_path):
            pdfmetrics.registerFont(TTFont("DejaVu", dejavu_path))
            pdfmetrics.registerFont(TTFont("DejaVu-Bold", dejavu_bold_path))
            font_regular = "DejaVu"
            font_bold = "DejaVu-Bold"
    except Exception:
        pass  # Fall back to Helvetica

    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        leftMargin=3 * cm,
        rightMargin=3 * cm,
        topMargin=2.5 * cm,
        bottomMargin=2.5 * cm,
    )

    accent = HexColor("#2E4057")
    label_color = HexColor("#4A6080")
    light_grey = HexColor("#666666")

    styles = getSampleStyleSheet()

    style_title = ParagraphStyle(
        "LesTitle",
        fontName=font_bold,
        fontSize=18,
        leading=22,
        textColor=accent,
        spaceAfter=6,
    )
    style_section_header = ParagraphStyle(
        "SectionHeader",
        fontName=font_bold,
        fontSize=13,
        leading=17,
        textColor=accent,
        spaceBefore=14,
        spaceAfter=4,
    )
    style_body = ParagraphStyle(
        "Body",
        fontName=font_regular,
        fontSize=10.5,
        leading=15,
        spaceAfter=4,
        allowMarkup=1,
    )
    style_bullet = ParagraphStyle(
        "Bullet",
        fontName=font_regular,
        fontSize=10.5,
        leading=15,
        leftIndent=14,
        bulletIndent=0,
        spaceAfter=3,
        allowMarkup=1,
    )
    style_quote = ParagraphStyle(
        "Quote",
        fontName=font_regular,
        fontSize=11,
        leading=16,
        leftIndent=0,
        firstLineIndent=0,
        textColor=light_grey,
        spaceAfter=6,
        allowMarkup=1,
        alignment=TA_LEFT,
    )
    style_label = ParagraphStyle(
        "Label",
        fontName=font_bold,
        fontSize=16,
        leading=22,
        textColor=light_grey,
        spaceAfter=10,
        spaceBefore=6,
    )

    def md_to_flowables(text, section_title_override=None, skip_h1=False):
        """Convert simple Markdown to ReportLab flowables."""
        flowables = []
        lines = text.split("\n")
        i = 0
        while i < len(lines):
            line = lines[i].rstrip()

            # H1 — skip if skip_h1=True (used on Opdracht page where section header already set)
            if line.startswith("# "):
                if not skip_h1:
                    content = line[2:].strip()
                    # Remove backslash-escaping of dots (e.g. "1\. Titel" → "1. Titel")
                    content = re.sub(r"(\d+)\\\.(\s)", r"\1.\2", content)
                    if section_title_override:
                        flowables.append(Paragraph(section_title_override, style_title))
                    else:
                        flowables.append(Paragraph(escape_xml(content), style_title))
                i += 1
                continue

            # H2
            if line.startswith("## "):
                content = line[3:].strip()
                flowables.append(Paragraph(escape_xml(content), style_section_header))
                i += 1
                continue

            # H3
            if line.startswith("### "):
                content = line[4:].strip()
                flowables.append(Paragraph(escape_xml(content), style_section_header))
                i += 1
                continue

            # Bullet
            if line.startswith("- "):
                content = line[2:].strip()
                flowables.append(Paragraph(
                    render(content),
                    style_bullet,
                    bulletText=u"•",
                ))
                i += 1
                continue

            # Numbered list (1. 2. etc.)
            m = re.match(r"^(\d+)\\\.\s+(.*)", line)  # escaped dot from markdown
            if m:
                content = m.group(1) + ". " + m.group(2).strip()
                flowables.append(Paragraph(render(content), style_body))
                i += 1
                continue

            m2 = re.match(r"^(\d+)\.\s+(.*)", line)
            if m2:
                content = m2.group(1) + ". " + m2.group(2).strip()
                flowables.append(Paragraph(render(content), style_body))
                i += 1
                continue

            # Quote (starts with > or with ")
            if line.startswith(">"):
                content = line[1:].strip().strip('"')
                flowables.append(Paragraph(u"“" + render(content) + u"”", style_quote))
                i += 1
                continue

            # Standalone quoted line
            if line.startswith('"') and line.endswith('"'):
                content = line.strip('"')
                flowables.append(Paragraph(u"“" + render(content) + u"”", style_quote))
                i += 1
                continue

            # HR
            if line.strip() in ("---", "***", "___"):
                flowables.append(HRFlowable(width="100%", thickness=0.5, color=light_grey, spaceAfter=6, spaceBefore=6))
                i += 1
                continue

            # Empty line → small spacer
            if line.strip() == "":
                flowables.append(Spacer(1, 4))
                i += 1
                continue

            # Normal paragraph
            if line.strip():
                flowables.append(Paragraph(render(line.strip()), style_body))

            i += 1
        return flowables

    def escape_xml(text):
        """Escape XML special characters for ReportLab (excluding already-valid markup tags)."""
        text = text.replace("&", "&amp;")
        text = text.replace("<", "&lt;")
        text = text.replace(">", "&gt;")
        return text

    def inline_md(text):
        """Convert inline Markdown bold/italic to ReportLab XML tags.

        Call AFTER escape_xml so that raw '<' / '>' in the source are already
        escaped before we inject our own valid <b>/<i> tags.
        """
        # Bold: **text** → <b>text</b>
        text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
        # Italic: *text* → <i>text</i>
        text = re.sub(r"\*(.+?)\*", r"<i>\1</i>", text)
        return text

    def render(text):
        """Escape XML then apply inline Markdown markup — correct call order."""
        return inline_md(escape_xml(text))

    story = []

    # ---- Samenvatting section ----
    story.append(Paragraph("SAMENVATTING", style_label))
    story += md_to_flowables(samenvatting_text)

    story.append(PageBreak())

    # ---- Opdracht section ----
    story.append(Paragraph("OPDRACHT", style_label))
    story += md_to_flowables(opdracht_text, skip_h1=True)

    doc.build(story)


def generate_intro_pdf_reportlab(intro_text, output_path):
    """Generate a single-page intro PDF using ReportLab.

    Layout: big title at the top, then content directly. No section label.
    No page break, no samenvatting/opdracht split.
    """
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import cm
    from reportlab.lib.colors import HexColor
    from reportlab.lib.enums import TA_LEFT
    from reportlab.platypus import (
        SimpleDocTemplate, Paragraph, Spacer, HRFlowable,
    )
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont

    font_regular = "Helvetica"
    font_bold = "Helvetica-Bold"
    try:
        dejavu_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
        dejavu_bold_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
        if os.path.exists(dejavu_path):
            pdfmetrics.registerFont(TTFont("DejaVu", dejavu_path))
            pdfmetrics.registerFont(TTFont("DejaVu-Bold", dejavu_bold_path))
            font_regular = "DejaVu"
            font_bold = "DejaVu-Bold"
    except Exception:
        pass

    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        leftMargin=3 * cm,
        rightMargin=3 * cm,
        topMargin=2.5 * cm,
        bottomMargin=2.5 * cm,
    )

    accent = HexColor("#2E4057")
    light_grey = HexColor("#666666")

    style_title = ParagraphStyle(
        "IntroTitle",
        fontName=font_bold,
        fontSize=18,
        leading=22,
        textColor=accent,
        spaceAfter=6,
    )
    style_section_header = ParagraphStyle(
        "IntroSectionHeader",
        fontName=font_bold,
        fontSize=13,
        leading=17,
        textColor=accent,
        spaceBefore=14,
        spaceAfter=4,
    )
    style_body = ParagraphStyle(
        "IntroBody",
        fontName=font_regular,
        fontSize=10.5,
        leading=15,
        spaceAfter=4,
        allowMarkup=1,
    )
    style_bullet = ParagraphStyle(
        "IntroBullet",
        fontName=font_regular,
        fontSize=10.5,
        leading=15,
        leftIndent=14,
        bulletIndent=0,
        spaceAfter=3,
        allowMarkup=1,
    )
    style_label = ParagraphStyle(
        "IntroLabel",
        fontName=font_bold,
        fontSize=16,
        leading=22,
        textColor=light_grey,
        spaceAfter=10,
        spaceBefore=6,
    )

    def escape_xml(text):
        text = text.replace("&", "&amp;")
        text = text.replace("<", "&lt;")
        text = text.replace(">", "&gt;")
        return text

    def inline_md(text):
        text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
        text = re.sub(r"\*(.+?)\*", r"<i>\1</i>", text)
        return text

    def render(text):
        return inline_md(escape_xml(text))

    def md_to_flowables(text, skip_h1=False):
        flowables = []
        lines = text.split("\n")
        i = 0
        while i < len(lines):
            line = lines[i].rstrip()

            if line.startswith("# "):
                if not skip_h1:
                    content = line[2:].strip()
                    content = re.sub(r"(\d+)\\\.(\s)", r"\1.\2", content)
                    flowables.append(Paragraph(escape_xml(content), style_title))
                i += 1
                continue

            if line.startswith("## "):
                content = line[3:].strip()
                flowables.append(Paragraph(escape_xml(content), style_section_header))
                i += 1
                continue

            if line.startswith("### "):
                content = line[4:].strip()
                flowables.append(Paragraph(escape_xml(content), style_section_header))
                i += 1
                continue

            if line.startswith("- ") or line.startswith("  * ") or line.startswith("* "):
                # Strip bullet prefix variants
                content = re.sub(r"^(\s*[-*])\s+", "", line).strip()
                flowables.append(Paragraph(
                    render(content),
                    style_bullet,
                    bulletText=u"•",
                ))
                i += 1
                continue

            if line.strip() in ("---", "***", "___"):
                flowables.append(HRFlowable(width="100%", thickness=0.5, color=light_grey, spaceAfter=6, spaceBefore=6))
                i += 1
                continue

            if line.strip() == "":
                flowables.append(Spacer(1, 4))
                i += 1
                continue

            if line.strip():
                flowables.append(Paragraph(render(line.strip()), style_body))

            i += 1
        return flowables

    # Extract the <h1> title from the intro text (first line starting with "# ")
    intro_title = None
    for line in intro_text.split("\n"):
        if line.startswith("# "):
            intro_title = line[2:].strip()
            intro_title = re.sub(r"(\d+)\\\.(\s)", r"\1.\2", intro_title)
            # Strip "Introductie - " prefix so only the real subject remains
            intro_title = re.sub(r"^Introductie\s*[-–]\s*", "", intro_title, flags=re.IGNORECASE)
            # Normalize separator: colon followed by space → semicolon + space
            intro_title = re.sub(r":\s+", "; ", intro_title)
            break

    story = []

    # ---- Section label: "INTRODUCTIE" (same style as "SAMENVATTING"/"OPDRACHT") ----
    story.append(Paragraph("INTRODUCTIE", style_label))

    # ---- Big lesson title (accent color, 18pt — same as lesson title) ----
    if intro_title:
        story.append(Paragraph(escape_xml(intro_title), style_title))

    # ---- Content: skip the h1 line since it's already rendered above ----
    story += md_to_flowables(intro_text, skip_h1=True)

    doc.build(story)


# ---------------------------------------------------------------------------
# Image-first layout (3-page: image | samenvatting | opdracht)
# ---------------------------------------------------------------------------

def generate_pdf_with_image_reportlab(lesson_name, jpg_path, samenvatting_text, opdracht_text, output_path):
    """Generate a 3-page lesson PDF: image page, samenvatting, opdracht."""
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.lib.units import cm
    from reportlab.lib.colors import HexColor
    from reportlab.lib.enums import TA_CENTER
    from reportlab.platypus import (Image, PageBreak, Paragraph, Spacer,
        HRFlowable, NextPageTemplate, Table, TableStyle)
    from reportlab.platypus.doctemplate import BaseDocTemplate, PageTemplate, Frame
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont

    font_regular = "Helvetica"; font_bold = "Helvetica-Bold"
    try:
        pdfmetrics.registerFont(TTFont("DejaVu", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
        pdfmetrics.registerFont(TTFont("DejaVu-Bold", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"))
        font_regular = "DejaVu"; font_bold = "DejaVu-Bold"
    except Exception:
        pass

    accent = HexColor("#2E4057"); light_grey = HexColor("#666666")
    style_label  = ParagraphStyle("Label",  fontName=font_bold,    fontSize=16, leading=22, textColor=light_grey, spaceAfter=10, spaceBefore=6)
    style_les_nr = ParagraphStyle("LesNr",  fontName=font_bold,    fontSize=48, leading=56, textColor=accent, spaceAfter=0, spaceBefore=0, alignment=TA_CENTER)
    style_h2     = ParagraphStyle("H2",     fontName=font_bold,    fontSize=13, leading=17, textColor=accent, spaceBefore=14, spaceAfter=4)
    style_body   = ParagraphStyle("Body",   fontName=font_regular, fontSize=10.5, leading=15, spaceAfter=4, allowMarkup=1)
    style_bullet = ParagraphStyle("Bullet", fontName=font_regular, fontSize=10.5, leading=15, leftIndent=14, spaceAfter=3, allowMarkup=1)
    style_quote  = ParagraphStyle("Quote",  fontName=font_regular, fontSize=11,   leading=16, textColor=light_grey, spaceAfter=6, allowMarkup=1)

    def esc(t): return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    def rend(t):
        t = esc(t)
        t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
        t = re.sub(r"\*(.+?)\*",     r"<i>\1</i>", t)
        return t

    def md_to_flowables(text, skip_h1=True):
        result = []
        for line in text.split("\n"):
            line = line.rstrip()
            if line.startswith("# "):
                if not skip_h1: result.append(Paragraph(esc(line[2:].strip()), style_label))
            elif line.startswith("## "): result.append(Paragraph(esc(line[3:].strip()), style_h2))
            elif line.startswith("- "): result.append(Paragraph(rend(line[2:].strip()), style_bullet, bulletText="•"))
            elif line.strip() in ("---", "***", "___"): result.append(HRFlowable(width="100%", thickness=0.5, color=light_grey))
            elif line.startswith(">"): result.append(Paragraph('"' + rend(line[1:].strip().strip('"')) + '"', style_quote))
            elif line.strip() == "": result.append(Spacer(1, 4))
            else: result.append(Paragraph(rend(line.strip()), style_body))
        while result and isinstance(result[0], Spacer):
            result.pop(0)
        return result

    W, H = A4
    img_side_margin = 5
    img_top_margin  = 1.5 * cm
    extra_spacing   = 20
    label_height    = 80 + extra_spacing

    if _PIL_AVAILABLE:
        orig_w, orig_h = PILImage.open(jpg_path).size
    else:
        orig_w, orig_h = 1440, 2560  # fallback assumption
    avail_w = W - 2*img_side_margin
    avail_h = H - 2*img_top_margin - label_height
    ratio = orig_w / orig_h
    if ratio * avail_h <= avail_w:
        img_h = avail_h; img_w = ratio * avail_h
    else:
        img_w = avail_w; img_h = avail_w / ratio

    m = re.match(r"Les (\d+)\.", lesson_name)
    les_nr = m.group(1) if m else "?"

    class ThreePageDoc(BaseDocTemplate):
        def __init__(self, filename, **kw):
            super().__init__(filename, **kw)
            img_frame  = Frame(img_side_margin, img_top_margin,
                               W - 2*img_side_margin, H - 2*img_top_margin,
                               leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0, id="img")
            norm_frame = Frame(3*cm, 2.5*cm, W - 6*cm, H - 5*cm, id="normal")
            self.addPageTemplates([
                PageTemplate(id="Image",  frames=[img_frame]),
                PageTemplate(id="Normal", frames=[norm_frame]),
            ])

    doc = ThreePageDoc(output_path, pagesize=A4)

    page1 = Table([
        [Paragraph(f"Les {les_nr}", style_les_nr)],
        [Spacer(1, extra_spacing)],
        [Image(jpg_path, width=img_w, height=img_h)],
    ], colWidths=[avail_w])
    page1.setStyle(TableStyle([
        ("ALIGN",        (0,0), (-1,-1), "CENTER"),
        ("VALIGN",       (0,0), (-1,-1), "TOP"),
        ("LEFTPADDING",  (0,0), (-1,-1), 0),
        ("RIGHTPADDING", (0,0), (-1,-1), 0),
        ("TOPPADDING",   (0,0), (-1,-1), 0),
        ("BOTTOMPADDING",(0,0), (-1,-1), 0),
    ]))

    story = [
        NextPageTemplate("Image"),
        page1,
        NextPageTemplate("Normal"),
        PageBreak(),
        Paragraph("SAMENVATTING", style_label),
        *md_to_flowables(samenvatting_text, skip_h1=True),
        PageBreak(),
        Paragraph("OPDRACHT", style_label),
        *md_to_flowables(opdracht_text, skip_h1=True),
    ]
    doc.build(story)


# ---------------------------------------------------------------------------
# Pandoc renderer (xelatex / pdflatex)
# ---------------------------------------------------------------------------

def generate_pdf_pandoc(engine, lesson_name, samenvatting_text, opdracht_text, output_path):
    """Generate PDF using pandoc + LaTeX engine."""
    combined = samenvatting_text + "\n\n\\newpage\n\n" + opdracht_text
    with tempfile.NamedTemporaryFile(suffix=".md", mode="w", encoding="utf-8", delete=False) as f:
        f.write(combined)
        tmp_md = f.name

    try:
        cmd = [
            "pandoc", tmp_md,
            "-o", output_path,
            f"--pdf-engine={engine}",
            "--variable", "geometry:margin=3cm",
            "--variable", "fontsize=11pt",
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            raise RuntimeError(result.stderr)
    finally:
        os.unlink(tmp_md)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def find_intro(folder):
    """Find intro .md file dynamically (any file matching Introductie*.md)."""
    matches = glob.glob(os.path.join(folder, "Introductie*.md"))
    return matches[0] if matches else None


def main():
    parser = argparse.ArgumentParser(description="Generate 365 Academy lesson PDFs")
    parser.add_argument("--folder", default=DEFAULT_FOLDER, help="Path to lesson folder")
    parser.add_argument(
        "--intro",
        action="store_true",
        help="Generate only the intro PDF (single-page, title + content only)",
    )
    args = parser.parse_args()

    folder = args.folder
    if not os.path.isdir(folder):
        print(f"ERROR: Folder not found: {folder}")
        sys.exit(1)

    engine = detect_engine()
    print(f"PDF engine: {engine}")
    print(f"Source folder: {folder}")
    print()

    # ---- Intro-only mode ----
    if args.intro:
        intro_md_path = find_intro(folder)
        if not intro_md_path:
            print(f"ERROR: No Introductie*.md found in {folder}")
            sys.exit(1)
        intro_pdf_path = os.path.splitext(intro_md_path)[0] + ".pdf"
        print(f"  Generating intro PDF from {os.path.basename(intro_md_path)} ...", end=" ", flush=True)
        try:
            intro_text = read_md(intro_md_path)
            generate_intro_pdf_reportlab(intro_text, intro_pdf_path)
            size_kb = os.path.getsize(intro_pdf_path) // 1024
            print(f"OK ({size_kb} KB)")
            print(f"\nDone. Intro PDF: {intro_pdf_path}")
        except Exception as e:
            print(f"ERROR: {e}")
            sys.exit(1)
        return

    # ---- Normal lesson mode ----
    lessons = find_lessons(folder)
    if not lessons:
        print("No lessons found.")
        sys.exit(0)

    print(f"Found {len(lessons)} lessons to process.\n")

    created = []
    errors = []

    for nr, lesson_name, sam_path, opdracht_path in lessons:
        output_path = os.path.join(folder, lesson_name + ".pdf")
        jpg_path = os.path.join(folder, lesson_name + ".jpg")
        print(f"  [{nr:>2}] {lesson_name} ...", end=" ", flush=True)
        try:
            samenvatting = read_md(sam_path)
            opdracht = strip_html_tags(read_md(opdracht_path))

            if os.path.exists(jpg_path):
                generate_pdf_with_image_reportlab(lesson_name, jpg_path, samenvatting, opdracht, output_path)
            elif engine == "reportlab":
                generate_pdf_reportlab(lesson_name, samenvatting, opdracht, output_path)
            else:
                generate_pdf_pandoc(engine, lesson_name, samenvatting, opdracht, output_path)

            size_kb = os.path.getsize(output_path) // 1024
            print(f"OK ({size_kb} KB)")
            created.append(lesson_name)
        except Exception as e:
            print(f"ERROR: {e}")
            errors.append((lesson_name, str(e)))

    print()
    print(f"Done. {len(created)} PDFs created, {len(errors)} errors.")
    if errors:
        print("\nErrors:")
        for name, err in errors:
            print(f"  - {name}: {err}")


if __name__ == "__main__":
    main()
