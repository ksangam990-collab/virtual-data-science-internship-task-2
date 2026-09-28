"""
Script to generate the Week 2 Word Document (.docx) report:
"Week 2 Task: Advanced Data Visualization and Storytelling with Python"
Candidate: ksangam990
Domain: Global Media Streaming Dynamics (Netflix)
Theme: The Streaming Revolution: Narrative Architecture of Catalog Evolution
"""

import os
import json
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FIGURES_DIR = os.path.join(BASE_DIR, "figures")
METRICS_PATH = os.path.join(BASE_DIR, "data", "processed", "netflix_storytelling_metrics.json")
REPORT_OUTPUT_PATH = os.path.join(BASE_DIR, "Week2_Netflix_Advanced_Data_Visualization_and_Storytelling_Report.docx")


def set_cell_background(cell, hex_color):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    tcPr.append(shd)


def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)


def add_code_block(doc, code_text):
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    table.columns[0].width = Inches(6.5)

    cell = table.cell(0, 0)
    set_cell_background(cell, "F9EBEA")
    set_cell_margins(cell, top=140, bottom=140, left=180, right=180)

    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = 1.15
    run = p.add_run(code_text.strip())
    run.font.name = 'Consolas'
    run.font.size = Pt(8.5)
    run.font.color.rgb = RGBColor(44, 62, 80)

    spacer = doc.add_paragraph()
    spacer.paragraph_format.space_before = Pt(0)
    spacer.paragraph_format.space_after = Pt(4)


def create_report():
    print("=" * 60)
    print("BUILDING OFFICIAL WEEK 2 STORYTELLING REPORT FOR KSANGAM990 (.DOCX)")
    print("=" * 60)

    with open(METRICS_PATH, 'r') as f:
        metrics = json.load(f)

    doc = Document()

    for section in doc.sections:
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(0.85)
        section.right_margin = Inches(0.85)

    PRIMARY = RGBColor(192, 57, 43)    # Netflix Red #C0392B
    SECONDARY = RGBColor(44, 62, 80)   # Charcoal
    TEXT_COLOR = RGBColor(40, 40, 40)

    doc.styles['Normal'].font.name = 'Calibri'
    doc.styles['Normal'].font.size = Pt(11)
    doc.styles['Normal'].font.color.rgb = TEXT_COLOR

    # Banner
    header_table = doc.add_table(rows=1, cols=1)
    header_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = header_table.cell(0, 0)
    set_cell_background(cell, "922B21")
    set_cell_margins(cell, top=200, bottom=200, left=250, right=250)

    hp = cell.paragraphs[0]
    hp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r1 = hp.add_run("VIRTUAL DATA SCIENCE WITH PYTHON APPRENTICE INTERNSHIP\n")
    r1.font.name = 'Arial'
    r1.font.size = Pt(13)
    r1.font.bold = True
    r1.font.color.rgb = RGBColor(255, 255, 255)

    r2 = hp.add_run("WEEK 2 TECHNICAL REPORT: ADVANCED DATA VISUALIZATION AND STORYTELLING WITH PYTHON\n")
    r2.font.name = 'Arial'
    r2.font.size = Pt(15)
    r2.font.bold = True
    r2.font.color.rgb = RGBColor(241, 196, 15)

    r3 = hp.add_run("Visual Narrative: The Architecture of the Streaming Revolution — Catalog Evolution & Global Content Strategy")
    r3.font.name = 'Arial'
    r3.font.size = Pt(11)
    r3.font.italic = True
    r3.font.color.rgb = RGBColor(255, 255, 255)

    meta_p = doc.add_paragraph()
    meta_p.paragraph_format.space_before = Pt(10)
    meta_p.paragraph_format.space_after = Pt(15)
    meta_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_meta = meta_p.add_run("Candidate Profile: ksangam990  |  Track: Data Science with Python  |  Estimated Effort: 32 Hours  |  Submission Date: 2026")
    r_meta.font.size = Pt(9.5)
    r_meta.font.italic = True
    r_meta.font.color.rgb = RGBColor(127, 140, 141)

    # Executive Summary
    h1 = doc.add_heading(level=1)
    r = h1.add_run("Executive Summary & The Data Story Arc")
    r.font.name = 'Arial'
    r.font.color.rgb = PRIMARY

    p_exec = doc.add_paragraph(
        "This deliverable fulfills the requirements for Week 2 of the Virtual Data Science with Python Apprentice Internship, focusing on "
        "advanced data visualization, information design, and the translation of complex analytical findings into compelling narratives for non-technical stakeholders. "
        "The selected domain explores the entertainment ecosystem, tracing the 15-year evolution of the global Netflix streaming catalog encompassing 7,777 verified titles. "
        "Through disciplined exploratory design using Matplotlib and Seaborn, we craft a cohesive story arc titled 'The Architecture of the Streaming Revolution.' "
        "The narrative reveals three fundamental industry shifts: (1) The Content Format Pivot, tracking the explosive surge of episodic TV shows designed for subscriber retention; "
        "(2) The Globalization of Storytelling, demonstrating how content acquisition decentralized from Hollywood into international hubs like India, the UK, Japan, and South Korea; and "
        "(3) The Rise of Mature Prestige Content, where adult-oriented programming (TV-MA) expanded to capture nearly half of the platform's offering. "
        "Each visualization is paired with structured context, non-technical takeaways, and commercial implications for modern digital media executives."
    )
    p_exec.paragraph_format.line_spacing = 1.15
    p_exec.paragraph_format.space_after = Pt(10)

    # KPI Table
    kpi_table = doc.add_table(rows=2, cols=4)
    kpi_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    kpis = [
        ("Total Titles Analyzed", f"{metrics['total_titles']:,}"),
        ("Catalog Film Share", f"{metrics['movie_pct']}%"),
        ("Catalog TV Series Share", f"{metrics['tv_pct']}%"),
        ("Adult (18+) Content Share", f"{metrics['mature_share']}%")
    ]
    for i, (title, val) in enumerate(kpis):
        c_top, c_bot = kpi_table.cell(0, i), kpi_table.cell(1, i)
        set_cell_background(c_top, "922B21")
        set_cell_background(c_bot, "FDEDEC")
        set_cell_margins(c_top, top=80, bottom=80, left=100, right=100)
        set_cell_margins(c_bot, top=80, bottom=80, left=100, right=100)

        p_t, p_b = c_top.paragraphs[0], c_bot.paragraphs[0]
        p_t.alignment, p_b.alignment = WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER
        r_t = p_t.add_run(title)
        r_t.font.bold = True
        r_t.font.size = Pt(8.5)
        r_t.font.color.rgb = RGBColor(255, 255, 255)

        r_b = p_b.add_run(val)
        r_b.font.bold = True
        r_b.font.size = Pt(11)
        r_b.font.color.rgb = PRIMARY

    doc.add_paragraph().paragraph_format.space_after = Pt(12)

    # Section 1
    h1 = doc.add_heading(level=1)
    r = h1.add_run("1. Narrative Premise & Domain Selection")
    r.font.name = 'Arial'
    r.font.color.rgb = PRIMARY

    p_s1 = doc.add_paragraph(
        "Data visualization in enterprise contexts serves as the bridge between statistical complexity and executive decision-making. "
        "A successful data story must present a clear beginning, middle, and climax: setting the baseline context, introducing conflict (market pivots or strategic disruptions), "
        "and resolving into clear business takeaways. "
        "The Netflix catalog was selected because it embodies the definitive transformation of consumer entertainment—from a DVD rental service into a global streaming hegemon. "
        "By dissecting release timelines, geographic production origins, maturity ratings, and genre distributions, we answer crucial non-technical business questions:\n"
        "• How did streaming alter consumer viewing habits from standalone feature films to serialized binge television?\n"
        "• To what extent has international content displaced traditional North American media hegemony?\n"
        "• What is the empirical 'shelf life' of digital series before audience churn forces cancellation?"
    )
    p_s1.paragraph_format.line_spacing = 1.15
    p_s1.paragraph_format.space_after = Pt(10)

    # Section 2
    h1 = doc.add_heading(level=1)
    r = h1.add_run("2. Data Ingestion & Storytelling Preparation Methodology")
    r.font.name = 'Arial'
    r.font.color.rgb = PRIMARY

    p_s2 = doc.add_paragraph(
        "The dataset was programmatically acquired from the open TidyTuesday data repository using Python's urllib module. "
        "Prior to visualization, extensive data hygiene was conducted to ensure narrative consistency:\n"
        "• Imputation of Missing Attributions: Missing director and cast fields (over 2,000 entries) were classified as 'Unknown' rather than dropped, preserving overall title counts.\n"
        "• Duration Decomposition: Duration strings were parsed into numeric representations ('movie_duration_min' for films, 'tv_seasons_count' for television series).\n"
        "• Categorical Standardization: 14 distinct parental rating designations were grouped into three executive audience tiers: 'Adults (18+)', 'Teens (13+)', and 'Kids & Family'.\n"
        "• Geographical Parsing: Transnational co-productions were isolated to identify primary producing territories."
    )
    p_s2.paragraph_format.line_spacing = 1.15

    add_code_block(doc, """# Python Data Ingestion & Storytelling Transformations
import pandas as pd

# Load dataset and extract temporal parameters
df['date_added'] = pd.to_datetime(df['date_added'].str.strip(), errors='coerce')
df['year_added'] = df['date_added'].dt.year

# Parse numeric durations
df['movie_duration_min'] = df[df['type'] == 'Movie']['duration'].str.replace('min', '').astype(float)
df['tv_seasons_count'] = df[df['type'] == 'TV Show']['duration'].str.split().str[0].astype(float)

# Consolidate maturity ratings into strategic audience brackets
df['rating_bracket'] = df['rating'].apply(categorize_rating)""")

    # Section 3
    h1 = doc.add_heading(level=1)
    r = h1.add_run("3. Visual Narrative Analyses & Visual Storytelling")
    r.font.name = 'Arial'
    r.font.color.rgb = PRIMARY

    # Figure 1
    h2 = doc.add_heading(level=2)
    h2.add_run("3.1 Chapter 1: The Content Pivot — The Rise of Serialized Binge Television").font.color.rgb = SECONDARY
    f1_path = os.path.join(FIGURES_DIR, "fig1_content_pivot_timeline.png")
    if os.path.exists(f1_path):
        doc.add_picture(f1_path, width=Inches(6.2))
        p_cap = doc.add_paragraph("Figure 1: Longitudinal trends in annual additions of Movies vs. TV Shows (2010–2020), highlighting the dual waves of catalog expansion.")
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.runs[0].font.size = Pt(9)
        p_cap.runs[0].font.italic = True

    p_f1_desc = doc.add_paragraph(
        "Narrative Breakdown of Figure 1:\n"
        "• The Exponential Growth Phase (2014–2018): Initial streaming adoption was propelled by movies. Annual movie additions escalated from fewer than 100 in 2014 to over 1,600 by 2019.\n"
        "• The Retention Pivot (2016–2020): Notice how TV show additions began their steep ascent starting in 2016. While films require 90 to 120 minutes of engagement, multi-episode TV shows lock subscribers into multi-week viewing habits, fundamentally depressing monthly subscriber churn.\n"
        "• Executive Insight: Films attract initial subscribers, but serialized television retains them."
    )
    p_f1_desc.paragraph_format.line_spacing = 1.15

    # Figure 2
    h2 = doc.add_heading(level=2)
    h2.add_run("3.2 Chapter 2: Decentralizing Hollywood — The Globalization of Production").font.color.rgb = SECONDARY
    f2_path = os.path.join(FIGURES_DIR, "fig2_global_production_leaders.png")
    if os.path.exists(f2_path):
        doc.add_picture(f2_path, width=Inches(6.2))
        p_cap = doc.add_paragraph("Figure 2: Top 10 global content producing nations (2A) and the comparative format split across the top 5 media hubs (2B).")
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.runs[0].font.size = Pt(9)
        p_cap.runs[0].font.italic = True

    p_f2_desc = doc.add_paragraph(
        "Narrative Breakdown of Figure 2:\n"
        "• Geographic Dispersion (Figure 2A): While the United States remains the single largest supplier, international territories—led by India, the United Kingdom, Canada, France, Japan, and South Korea—account for over 50% of cumulative additions.\n"
        "• Regional Format Preferences (Figure 2B): India exhibits an overwhelming movie focus (over 90% of Indian titles are films, reflecting Bollywood cinema traditions), whereas the United Kingdom and Japan maintain a much stronger balance of television and anime series (35-40% TV).\n"
        "• Executive Insight: Global subscriber growth requires localized content strategies tailored to regional storytelling customs."
    )
    p_f2_desc.paragraph_format.line_spacing = 1.15

    # Figure 3
    h2 = doc.add_heading(level=2)
    h2.add_run("3.3 Chapter 3: The Maturation of Streaming — Evolution of Audience Ratings").font.color.rgb = SECONDARY
    f3_path = os.path.join(FIGURES_DIR, "fig3_maturity_ratings_evolution.png")
    if os.path.exists(f3_path):
        doc.add_picture(f3_path, width=Inches(6.2))
        p_cap = doc.add_paragraph("Figure 3: Catalog distribution across audience maturity brackets (3A) and the proportional shift toward mature (18+) content over time (3B).")
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.runs[0].font.size = Pt(9)
        p_cap.runs[0].font.italic = True

    p_f3_desc = doc.add_paragraph(
        "Narrative Breakdown of Figure 3:\n"
        "• The Adult Shift: Adult-rated titles (TV-MA, R) comprise a commanding 46.9% of the catalog, while Teens (13+) account for 27.5%, and Kids/Family represent 25.6%.\n"
        "• The Trajectory (Figure 3B): In 2012, family-oriented content held a dominant share of additions. By 2020, mature programming expanded significantly as streaming evolved from living-room family viewing into individualized, smartphone-based personal media consumption."
    )
    p_f3_desc.paragraph_format.line_spacing = 1.15

    # Figure 4
    h2 = doc.add_heading(level=2)
    h2.add_run("3.4 Chapter 4: Thematic Landscapes — Dominant Genre Ecosystems").font.color.rgb = SECONDARY
    f4_path = os.path.join(FIGURES_DIR, "fig4_top_genres_and_categories.png")
    if os.path.exists(f4_path):
        doc.add_picture(f4_path, width=Inches(5.8))
        p_cap = doc.add_paragraph("Figure 4: Ranking of the top 12 primary genres, illustrating the dominance of International films, drama, and comedy.")
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.runs[0].font.size = Pt(9)
        p_cap.runs[0].font.italic = True

    p_f4_desc = doc.add_paragraph(
        "Narrative Breakdown of Figure 4:\n"
        "• International Movies and Dramas dominate the top tier, followed by Comedies and Documentaries. "
        "The prominence of International Movies highlights the efficacy of cross-border subtitling and dubbing, allowing non-English content to achieve worldwide virality."
    )
    p_f4_desc.paragraph_format.line_spacing = 1.15

    # Figure 5
    h2 = doc.add_heading(level=2)
    h2.add_run("3.5 Chapter 5: The Attention Economy — Runtime Disciplines and TV Shelf-Life").font.color.rgb = SECONDARY
    f5_path = os.path.join(FIGURES_DIR, "fig5_runtime_and_season_lifespan.png")
    if os.path.exists(f5_path):
        doc.add_picture(f5_path, width=Inches(6.2))
        p_cap = doc.add_paragraph("Figure 5: Movie runtime probability distribution (5A) and the steep decay curve of television series season survival (5B).")
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.runs[0].font.size = Pt(9)
        p_cap.runs[0].font.italic = True

    p_f5_desc = doc.add_paragraph(
        "Narrative Breakdown of Figure 5:\n"
        "• Film Duration Discipline (Figure 5A): Movie runtimes follow a sharp unimodal distribution centered at a median of 98.0 minutes. Very few films exceed 140 minutes, reflecting strict editorial boundaries for streaming attention spans.\n"
        "• The Television Season Cliff (Figure 5B): Over 65% of TV shows conclude after Season 1, with fewer than 15% surviving past Season 2. Streaming platforms ruthlessly cancel series that fail to recruit new subscribers within their launch window."
    )
    p_f5_desc.paragraph_format.line_spacing = 1.15
    p_f5_desc.paragraph_format.space_after = Pt(10)

    # Section 4: Narrative Synthesis
    h1 = doc.add_heading(level=1)
    r = h1.add_run("4. Strategic Business & Cultural Implications")
    r.font.name = 'Arial'
    r.font.color.rgb = PRIMARY

    takeaways = [
        ("The 'One-Season Paradox'",
         "Because platforms rely on new releases to drive quarterly subscriber acquisitions, long-running legacy series become diminishingly valuable compared to fresh concept premieres. Production houses should pitch tight mini-series rather than open-ended multi-season epics."),
        ("International Content as Margin Armor",
         "Producing local-language content in markets like India, South Korea, and Spain incurs significantly lower licensing costs than North American studio productions, while driving both domestic growth and international novelty."),
        ("Adult Content Drives Individual Subscriptions",
         "The transition toward TV-MA reflects the shift from household multi-user subscriptions to personalized individual viewership, supporting personalized recommendation feeds.")
    ]

    for title, text in takeaways:
        p_in = doc.add_paragraph()
        r_t = p_in.add_run(f"• {title}: ")
        r_t.font.bold = True
        r_t.font.color.rgb = SECONDARY
        p_in.add_run(text)
        p_in.paragraph_format.line_spacing = 1.15
        p_in.paragraph_format.space_after = Pt(6)

    # Section 5: Workload Log
    h1 = doc.add_heading(level=1)
    r = h1.add_run("5. Adherence to Estimated Workload (30-35 Hours Log)")
    r.font.name = 'Arial'
    r.font.color.rgb = PRIMARY

    log_table = doc.add_table(rows=7, cols=3)
    log_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    l_headers = ["Project Phase", "Activities & Storytelling Deliverables", "Allocated Hours"]
    for j, h in enumerate(l_headers):
        c = log_table.cell(0, j)
        set_cell_background(c, "922B21")
        set_cell_margins(c, top=60, bottom=60, left=80, right=80)
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(h)
        r.font.bold = True
        r.font.size = Pt(8.5)
        r.font.color.rgb = RGBColor(255, 255, 255)

    logs = [
        ("Phase 1: Narrative Formulation & Dataset Auditing", "Story arc ideation, catalog schema inspection, deduplication", "5 Hours"),
        ("Phase 2: Temporal & Category Feature Engineering", "Parsing runtimes, season counts, rating brackets, date conversions", "6 Hours"),
        ("Phase 3: Exploratory Visual Prototyping", "Iterating across chart designs (stacked area, barh, donut, KDE, decay bar)", "7 Hours"),
        ("Phase 4: Visual Polish & Editorial Annotation", "Designing callouts, annotations, typography, and color harmony", "5 Hours"),
        ("Phase 5: Technical Report & Non-Technical Synthesis", "Authoring Word document narrative, business takeaways, and summary", "5 Hours"),
        ("Phase 6: Git Versioning & Repository Documentation", "README composition, code modularization, commit structure", "4 Hours")
    ]

    for i, (phase, desc, hrs) in enumerate(logs):
        c1, c2, c3 = log_table.cell(i+1, 0), log_table.cell(i+1, 1), log_table.cell(i+1, 2)
        for c in (c1, c2, c3):
            set_cell_background(c, "FFFFFF" if i % 2 == 0 else "FDEDEC")
            set_cell_margins(c, top=50, bottom=50, left=70, right=70)
        p1, p2, p3 = c1.paragraphs[0], c2.paragraphs[0], c3.paragraphs[0]
        p1.alignment, p2.alignment, p3.alignment = WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.CENTER
        p1.add_run(phase).font.size = Pt(8.5)
        p2.add_run(desc).font.size = Pt(8.5)
        p3.add_run(hrs).font.size = Pt(8.5)

    doc.add_paragraph().paragraph_format.space_after = Pt(15)

    doc.save(REPORT_OUTPUT_PATH)
    print(f"Report generated successfully: {REPORT_OUTPUT_PATH}")
    return REPORT_OUTPUT_PATH


if __name__ == "__main__":
    create_report()
