# Virtual Data Science with Python Apprentice Intern
## Week 2: Advanced Data Visualization and Storytelling with Python

![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![Seaborn](https://img.shields.io/badge/Seaborn-Visual%20Storytelling-e50914.svg)
![Status](https://img.shields.io/badge/Milestone-Week%202%20Completed-brightgreen.svg)

---

### 📖 The Narrative: Architecture of the Streaming Revolution
This repository contains the complete Week 2 deliverables for **ksangam990** under the **Virtual Data Science with Python Apprentice Internship**. This milestone emphasizes the translation of complex tabular datasets into intuitive, high-impact visual narratives tailored for non-technical executives and content strategists.

Investigating **7,777 verified titles from the global Netflix catalog**, the project dissects how streaming dismantled traditional media distribution over the last 15 years through three strategic acts:
1. **The Format Pivot:** How episodic television additions accelerated from 2016 onward to depress subscriber churn.
2. **The Globalization of Production:** How international storytelling hubs (India, UK, Japan, South Korea) decentralized Hollywood's historic monopoly.
3. **The Rise of Adult Prestige Media:** The demographic shift toward mature, individualized smartphone viewing (TV-MA).

---

### 📂 Directory Layout
```text
netflix-data-storytelling-ksangam990/
├── analysis_pipeline.py                    # Complete data preparation & visual storytelling engine
├── generate_docx_report.py                 # Automated Word document narrative generator
├── Week2_Netflix_Advanced_Data_Visualization_and_Storytelling_Report.docx # Official submission document (< 600 KB)
├── requirements.txt                        # Python dependencies
├── .gitignore                              # Git exclusion rules
├── README.md                               # Project documentation & storytelling insights
├── data/
│   ├── raw/
│   │   └── netflix_titles_raw.csv          # Raw catalog data (7,787 rows)
│   └── processed/
│       ├── netflix_titles_cleaned.csv      # Processed dataset with parsed durations and ratings
│       └── netflix_storytelling_metrics.json # Serialized storytelling KPIs
└── figures/
    ├── fig1_content_pivot_timeline.png     # Longitudinal timeline of Movies vs. TV Shows (2010–2020)
    ├── fig2_global_production_leaders.png  # Top 10 content producing nations & format mix
    ├── fig3_maturity_ratings_evolution.png # Content maturity distribution & adult programming shift
    ├── fig4_top_genres_and_categories.png  # Top 12 primary genre ranking
    └── fig5_runtime_and_season_lifespan.png# Film runtime distribution & TV show season decay curve
```

---

### 📊 Key Narrative Takeaways

| Storytelling Dimension | Empirical Observation | Commercial Takeaway |
| :--- | :--- | :--- |
| **Catalog Medium Split** | 69.1% Movies / 30.9% TV Shows | Films drive initial subscriptions; television series drive retention |
| **The 2016 Turning Point** | TV additions surged 400% between 2016–2019 | Transition from cinema repository to serialized binge-watching |
| **Global Content Share** | Over 50% produced outside the US | Localized production lowers licensing costs while diversifying appeal |
| **Maturity Dominance** | 46.9% Adult (TV-MA / R) | Shift from family living-room viewing to individual mobile streaming |
| **Movie Duration Discipline** | Median runtime strictly 98.0 minutes | Compact 90–100 min runtime sweet spot for modern digital attention |
| **The Television Cliff** | 65%+ of series conclude after Season 1 | Ruthless cancellation threshold for shows failing launch recruitment |

---

### 🚀 Getting Started

```bash
# 1. Clone repository
git clone https://github.com/ksangam990-collab/virtual-data-science-internship-task-2.git
cd virtual-data-science-internship-task-2

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run analysis pipeline & generate charts
python analysis_pipeline.py

# 4. Compile Word Document Report
python generate_docx_report.py
```

---
**Candidate:** ksangam990  
**Internship:** Virtual Data Science with Python Apprentice Intern  
**Adherence to Workload:** 32 Hours Logged  
