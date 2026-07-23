import os
import sys
import re
import html
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT

def clean_inline(text):
    # Escape XML characters
    text = html.escape(text, quote=False)
    # Replace **bold** with <b>bold</b>
    text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
    # Replace `code` with <font name="Courier" color="#1E293B">code</font>
    text = re.sub(r'`(.*?)`', r'<font name="Courier" size="8.5" color="#0F172A"><b>\1</b></font>', text)
    return text

def create_resume_pdf():
    md_file_path = r"c:\Users\rohit\Downloads\concept clear\Rohit_Mondal_Resume_updated.md"
    pdf_file_path = r"c:\Users\rohit\Downloads\concept clear\Rohit_Mondal_Resume_updated.pdf"

    if not os.path.exists(md_file_path):
        print(f"Error: {md_file_path} not found.")
        sys.exit(1)

    with open(md_file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    doc = SimpleDocTemplate(
        pdf_file_path,
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=36,
        bottomMargin=36
    )

    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=colors.HexColor('#0F172A'),
        alignment=TA_CENTER
    )

    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=15,
        textColor=colors.HexColor('#2563EB'),
        alignment=TA_CENTER
    )

    contact_style = ParagraphStyle(
        'DocContact',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor('#475569'),
        alignment=TA_CENTER
    )

    h1_style = ParagraphStyle(
        'Heading1_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=17,
        textColor=colors.HexColor('#0F172A'),
        spaceBefore=10,
        spaceAfter=4
    )

    h2_style = ParagraphStyle(
        'Heading2_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=15,
        textColor=colors.HexColor('#1E3A8A'),
        spaceBefore=8,
        spaceAfter=4
    )

    h3_style = ParagraphStyle(
        'Heading3_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=14,
        textColor=colors.HexColor('#0369A1'),
        spaceBefore=6,
        spaceAfter=3
    )

    body_style = ParagraphStyle(
        'Body_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor('#334155'),
        alignment=TA_LEFT,
        spaceAfter=3
    )

    bullet_style = ParagraphStyle(
        'Bullet_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor('#334155'),
        leftIndent=12,
        spaceAfter=2
    )

    code_style = ParagraphStyle(
        'Code_Custom',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=8,
        leading=11,
        textColor=colors.HexColor('#0F172A'),
        backColor=colors.HexColor('#F8FAFC'),
        borderColor=colors.HexColor('#E2E8F0'),
        borderWidth=0.5,
        borderPadding=6,
        spaceBefore=3,
        spaceAfter=5,
        leftIndent=10
    )

    story = []

    in_code_block = False
    code_lines = []

    for line in lines:
        raw_line = line.rstrip('\r\n')
        stripped = raw_line.strip()

        # Handle Code Blocks
        if stripped.startswith("```"):
            if in_code_block:
                # End of code block
                code_text = "<br/>".join([html.escape(c, quote=False).replace(" ", "&nbsp;") for c in code_lines])
                story.append(Paragraph(code_text, code_style))
                code_lines = []
                in_code_block = False
            else:
                in_code_block = True
                code_lines = []
            continue

        if in_code_block:
            code_lines.append(raw_line)
            continue

        if not stripped:
            continue

        # Header section parsing
        if stripped == "# ROHIT MONDAL":
            story.append(Paragraph("ROHIT MONDAL", title_style))
            story.append(Spacer(1, 2))
            continue

        if stripped == "**Full-Stack Engineer | AI Integrator**":
            story.append(Paragraph("Full-Stack Engineer | AI Integrator", subtitle_style))
            story.append(Spacer(1, 4))
            continue

        if "rohit.simbanic2023@gmail.com" in stripped:
            contact_text = "rohit.simbanic2023@gmail.com &nbsp;|&nbsp; rohit-fullstack-ai.in &nbsp;|&nbsp; linkedin.com/in/rohit-m-552776aa &nbsp;|&nbsp; github.com/rohit-simbanic"
            story.append(Paragraph(contact_text, contact_style))
            story.append(Spacer(1, 4))
            story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#CBD5E1"), spaceAfter=8))
            continue

        if stripped.startswith("## "):
            heading_text = stripped[3:].strip()
            story.append(Spacer(1, 4))
            story.append(Paragraph(clean_inline(heading_text), h1_style))
            story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#94A3B8"), spaceAfter=6))
            continue

        if stripped.startswith("### "):
            heading_text = stripped[4:].strip()
            story.append(Paragraph(clean_inline(heading_text), h2_style))
            continue

        if stripped.startswith("---"):
            story.append(Spacer(1, 2))
            story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#E2E8F0"), spaceAfter=4))
            continue

        # Bullet points
        if stripped.startswith("* ") or stripped.startswith("- ") or stripped.startswith("• "):
            content = stripped[2:].strip()
            story.append(Paragraph(f"• {clean_inline(content)}", bullet_style))
            continue

        # Questions (Q1:, Q2:, etc.)
        if re.match(r'^Q\d+:', stripped):
            story.append(Spacer(1, 4))
            story.append(Paragraph(clean_inline(stripped), h3_style))
            continue

        # Regular text
        story.append(Paragraph(clean_inline(stripped), body_style))

    doc.build(story)
    print(f"Successfully generated PDF: {pdf_file_path}")

if __name__ == "__main__":
    create_resume_pdf()
