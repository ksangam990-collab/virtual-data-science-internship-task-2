"""
Week 2 Task: Advanced Data Visualization and Storytelling with Python
Candidate: ksangam990
Domain: Global Media Streaming & Entertainment Analytics (Netflix Catalog)
Theme: The Streaming Revolution: 15 Years of Catalog Evolution, Global Diversification, and Binge Culture
"""

import os
import urllib.request
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import json
from PIL import Image

# Aesthetic storytelling style
sns.set_theme(style="whitegrid")
plt.rcParams.update({
    'font.sans-serif': 'Arial',
    'font.family': 'sans-serif',
    'figure.titlesize': 13,
    'axes.titlesize': 11,
    'axes.labelsize': 10,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'figure.autolayout': True
})

DATA_RAW_URL = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-04-20/netflix_titles.csv"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RAW_DATA_PATH = os.path.join(BASE_DIR, "data", "raw", "netflix_titles_raw.csv")
CLEANED_DATA_PATH = os.path.join(BASE_DIR, "data", "processed", "netflix_titles_cleaned.csv")
FIGURES_DIR = os.path.join(BASE_DIR, "figures")
METRICS_PATH = os.path.join(BASE_DIR, "data", "processed", "netflix_storytelling_metrics.json")


def acquire_data():
    """Acquires raw Netflix titles dataset from public repository."""
    print("=" * 60)
    print("STEP 1: DATA ACQUISITION")
    print("=" * 60)
    os.makedirs(os.path.dirname(RAW_DATA_PATH), exist_ok=True)
    if not os.path.exists(RAW_DATA_PATH):
        print(f"Downloading Netflix catalog from: {DATA_RAW_URL}...")
        urllib.request.urlretrieve(DATA_RAW_URL, RAW_DATA_PATH)
        print(f"Raw data saved to: {RAW_DATA_PATH}")
    else:
        print(f"Raw data already exists at: {RAW_DATA_PATH}")

    df_raw = pd.read_csv(RAW_DATA_PATH)
    print(f"Acquired catalog shape: {df_raw.shape[0]} titles, {df_raw.shape[1]} features")
    return df_raw


def clean_and_prepare(df_raw):
    """Cleans data and prepares features for narrative visualization."""
    print("\n" + "=" * 60)
    print("STEP 2: DATA CLEANING & STORYTELLING FEATURE ENGINEERING")
    print("=" * 60)

    df = df_raw.copy()

    # 1. Deduplication
    dup_count = int(df.duplicated().sum())
    print(f"Duplicate titles detected: {dup_count}")

    # 2. Text sanitization
    for col in ['title', 'director', 'cast', 'country', 'rating', 'listed_in']:
        df[col] = df[col].astype(str).str.strip()

    # 3. Missing Value Handling
    df['director'] = df['director'].replace('nan', 'Unknown Director')
    df['cast'] = df['cast'].replace('nan', 'Unknown Cast')
    df['country'] = df['country'].replace('nan', 'Unknown Country')
    df['rating'] = df['rating'].replace(['nan', ''], 'TV-MA')  # Mode imputation

    # 4. Date parsing
    df['date_added'] = pd.to_datetime(df['date_added'].str.strip(), errors='coerce')
    df['year_added'] = df['date_added'].dt.year
    df['month_added'] = df['date_added'].dt.month_name()

    # Filter out entries prior to streaming surge or unverified future dates
    df = df[df['year_added'] >= 2008].copy()
    df['year_added'] = df['year_added'].astype(int)

    # 5. Extract duration metrics
    def parse_movie_duration(row):
        if row['type'] == 'Movie' and 'min' in str(row['duration']):
            try:
                return float(str(row['duration']).replace('min', '').strip())
            except:
                return np.nan
        return np.nan

    def parse_tv_seasons(row):
        if row['type'] == 'TV Show':
            try:
                return int(str(row['duration']).split()[0])
            except:
                return 1
        return np.nan

    df['movie_duration_min'] = df.apply(parse_movie_duration, axis=1)
    df['tv_seasons_count'] = df.apply(parse_tv_seasons, axis=1)

    # 6. Primary Country and Primary Genre
    df['primary_country'] = df['country'].apply(lambda x: str(x).split(',')[0].strip() if pd.notna(x) and str(x) not in ['Unknown Country', 'nan', ''] else 'Unknown')
    df['primary_genre'] = df['listed_in'].apply(lambda x: str(x).split(',')[0].strip() if pd.notna(x) else 'Other')

    # 7. Rating Tier categorization
    def categorize_rating(r):
        adults = ['TV-MA', 'R', 'NC-17', 'NR', 'UR']
        teens = ['TV-14', 'PG-13']
        kids = ['TV-PG', 'PG', 'TV-Y', 'TV-Y7', 'TV-Y7-FV', 'G']
        if r in adults:
            return 'Adults (18+)'
        elif r in teens:
            return 'Teens (13+)'
        elif r in kids:
            return 'Kids & Family'
        return 'Other / Unrated'

    df['rating_bracket'] = df['rating'].apply(categorize_rating)

    # Save cleaned
    os.makedirs(os.path.dirname(CLEANED_DATA_PATH), exist_ok=True)
    df.to_csv(CLEANED_DATA_PATH, index=False)
    print(f"Cleaned dataset saved: {CLEANED_DATA_PATH} ({len(df)} titles)")
    return df


def generate_storytelling_visualizations(df):
    """Generates 5 advanced storytelling visualizations."""
    print("\n" + "=" * 60)
    print("STEP 3: ADVANCED DATA STORYTELLING VISUALIZATIONS")
    print("=" * 60)
    os.makedirs(FIGURES_DIR, exist_ok=True)
    fig_paths = {}

    # -------------------------------------------------------------------------
    # FIGURE 1: The Great Pivot: Movies vs TV Shows Added (2008 - 2020)
    # -------------------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(11, 5.2))
    df_timeline = df[(df['year_added'] >= 2010) & (df['year_added'] <= 2020)]
    pivot_data = df_timeline.groupby(['year_added', 'type']).size().unstack(fill_value=0)

    ax.plot(pivot_data.index, pivot_data['Movie'], marker='o', linewidth=3, color='#e50914', label='Movies')
    ax.plot(pivot_data.index, pivot_data['TV Show'], marker='s', linewidth=3, color='#221f1f', linestyle='--', label='TV Shows')
    ax.fill_between(pivot_data.index, pivot_data['Movie'], alpha=0.15, color='#e50914')
    ax.fill_between(pivot_data.index, pivot_data['TV Show'], alpha=0.1, color='#221f1f')

    # Annotations to tell the story
    ax.annotate('Streaming Expansion Era\n(Explosive film catalog growth)', xy=(2016, 258), xytext=(2011.5, 600),
                arrowprops=dict(facecolor='#333333', arrowstyle='->', lw=1.2), fontsize=9.5, fontweight='bold')
    ax.annotate('Binge TV Boom:\nTV Show additions accelerate', xy=(2019, 650), xytext=(2015.5, 950),
                arrowprops=dict(facecolor='#333333', arrowstyle='->', lw=1.2), fontsize=9.5, fontweight='bold')

    ax.set_title('Figure 1: The Content Strategy Evolution — Annual Additions of Movies vs. TV Shows (2010–2020)', fontsize=12, fontweight='bold', pad=12)
    ax.set_xlabel('Year Cataloged on Platform', fontsize=11)
    ax.set_ylabel('Annual Titles Added', fontsize=11)
    ax.legend(title='Content Medium', loc='upper left', frameon=True)
    ax.set_xticks(range(2010, 2021))
    
    f1_path = os.path.join(FIGURES_DIR, "fig1_content_pivot_timeline.png")
    plt.savefig(f1_path, dpi=160)
    plt.close()
    fig_paths['fig1'] = f1_path
    print(f"Generated: {f1_path}")

    # -------------------------------------------------------------------------
    # FIGURE 2: Global Production Hubs (Top 10 Nations)
    # -------------------------------------------------------------------------
    fig, axes = plt.subplots(1, 2, figsize=(13, 5))
    top_countries = df[df['primary_country'] != 'Unknown']['primary_country'].value_counts().head(10).reset_index()
    top_countries.columns = ['Country', 'TitleCount']

    b = sns.barplot(data=top_countries, y='Country', x='TitleCount', palette='Reds_r', ax=axes[0], hue='Country', legend=False)
    axes[0].set_title('Figure 2A: Top 10 Content Producing Nations on Netflix', fontsize=11, fontweight='bold')
    axes[0].set_xlabel('Total Titles in Catalog')
    for p in b.patches:
        w = p.get_width()
        axes[0].text(w + 25, p.get_y() + p.get_height()/2., f'{int(w):,}', va='center', fontsize=8.5, fontweight='bold')

    # Media Type Share in Top 5 Countries
    top5_names = top_countries['Country'].head(5).tolist()
    top5_df = df[df['primary_country'].isin(top5_names)]
    c_type = top5_df.groupby(['primary_country', 'type']).size().unstack(fill_value=0)
    c_type_pct = (c_type.div(c_type.sum(axis=1), axis=0) * 100).loc[top5_names]

    c_type_pct.plot(kind='barh', stacked=True, color=['#e50914', '#2b2b2b'], ax=axes[1], width=0.6)
    axes[1].set_title('Figure 2B: Movies vs. TV Shows Mix in Top 5 Nations (%)', fontsize=11, fontweight='bold')
    axes[1].set_xlabel('Proportion (%)')
    axes[1].set_ylabel('')
    axes[1].legend(title='Format', loc='lower right')
    for c in axes[1].containers:
        axes[1].bar_label(c, fmt='%.0f%%', label_type='center', color='white', fontweight='bold', fontsize=8)

    plt.tight_layout()
    f2_path = os.path.join(FIGURES_DIR, "fig2_global_production_leaders.png")
    plt.savefig(f2_path, dpi=160)
    plt.close()
    fig_paths['fig2'] = f2_path
    print(f"Generated: {f2_path}")

    # -------------------------------------------------------------------------
    # FIGURE 3: Maturity Rating Architecture
    # -------------------------------------------------------------------------
    fig, axes = plt.subplots(1, 2, figsize=(13, 5))
    bracket_counts = df['rating_bracket'].value_counts()
    colors = ['#c0392b', '#2980b9', '#27ae60', '#7f8c8d']
    axes[0].pie(bracket_counts, labels=bracket_counts.index, autopct='%1.1f%%', startangle=140,
                colors=colors, wedgeprops=dict(width=0.42, edgecolor='white', linewidth=2))
    axes[0].set_title('Figure 3A: Catalog Content Maturity Share', fontsize=11, fontweight='bold')

    # Evolution of Adults vs Kids/Family content additions over time
    bracket_timeline = df[(df['year_added'] >= 2012) & (df['year_added'] <= 2020)].groupby(
        ['year_added', 'rating_bracket']).size().unstack(fill_value=0)
    b_pct = bracket_timeline.div(bracket_timeline.sum(axis=1), axis=0) * 100
    
    b_pct[['Adults (18+)', 'Teens (13+)', 'Kids & Family']].plot(
        kind='area', stacked=True, color=['#c0392b', '#2980b9', '#27ae60'], alpha=0.8, ax=axes[1])
    axes[1].set_title('Figure 3B: Shift Toward Mature Audience Content Over Time (%)', fontsize=11, fontweight='bold')
    axes[1].set_ylabel('Share of Additions (%)')
    axes[1].set_xlabel('Year Added')
    axes[1].legend(title='Audience Segment', loc='lower left')

    plt.tight_layout()
    f3_path = os.path.join(FIGURES_DIR, "fig3_maturity_ratings_evolution.png")
    plt.savefig(f3_path, dpi=160)
    plt.close()
    fig_paths['fig3'] = f3_path
    print(f"Generated: {f3_path}")

    # -------------------------------------------------------------------------
    # FIGURE 4: Genre Landscape
    # -------------------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(11, 5.5))
    top_genres = df['primary_genre'].value_counts().head(12).reset_index()
    top_genres.columns = ['Genre', 'Count']
    
    bg = sns.barplot(data=top_genres, y='Genre', x='Count', palette='mako', ax=ax, hue='Genre', legend=False)
    ax.set_title('Figure 4: Dominant Thematic Categories — Top 12 Primary Genres', fontsize=12, fontweight='bold', pad=12)
    ax.set_xlabel('Number of Catalog Titles', fontsize=11)
    for p in bg.patches:
        w = p.get_width()
        ax.text(w + 15, p.get_y() + p.get_height()/2., f'{int(w):,}', va='center', fontsize=9, fontweight='bold')

    plt.tight_layout()
    f4_path = os.path.join(FIGURES_DIR, "fig4_top_genres_and_categories.png")
    plt.savefig(f4_path, dpi=160)
    plt.close()
    fig_paths['fig4'] = f4_path
    print(f"Generated: {f4_path}")

    # -------------------------------------------------------------------------
    # FIGURE 5: Runtime & Series Lifespan Dynamics
    # -------------------------------------------------------------------------
    fig, axes = plt.subplots(1, 2, figsize=(13, 5))

    # Subplot A: Movie Duration Distribution
    movies_df = df[df['type'] == 'Movie'].dropna(subset=['movie_duration_min'])
    sns.histplot(movies_df['movie_duration_min'], bins=35, kde=True, color='#e50914', ax=axes[0])
    axes[0].axvline(movies_df['movie_duration_min'].median(), color='black', linestyle='--', linewidth=1.5,
                    label=f"Median Duration: {int(movies_df['movie_duration_min'].median())} mins")
    axes[0].set_title('Figure 5A: Film Runtime Distribution (Minutes)', fontsize=11, fontweight='bold')
    axes[0].set_xlabel('Duration (Minutes)')
    axes[0].set_ylabel('Frequency')
    axes[0].legend(loc='upper right')

    # Subplot B: TV Show Season Counts (Decay Curve)
    tv_df = df[df['type'] == 'TV Show'].dropna(subset=['tv_seasons_count'])
    season_counts = tv_df['tv_seasons_count'].value_counts().head(8).sort_index().reset_index()
    season_counts.columns = ['Seasons', 'ShowCount']
    sb = sns.barplot(data=season_counts, x='Seasons', y='ShowCount', palette='copper_r', ax=axes[1], hue='Seasons', legend=False)
    axes[1].set_title('Figure 5B: The Television Shelf-Life — Decay of Multi-Season Series', fontsize=11, fontweight='bold')
    axes[1].set_xlabel('Number of Seasons Released')
    axes[1].set_ylabel('Number of TV Shows')
    for p in sb.patches:
        h = p.get_height()
        axes[1].text(p.get_x() + p.get_width()/2., h + 20, f'{int(h)}', ha='center', fontsize=8.5, fontweight='bold')

    plt.tight_layout()
    f5_path = os.path.join(FIGURES_DIR, "fig5_runtime_and_season_lifespan.png")
    plt.savefig(f5_path, dpi=160)
    plt.close()
    fig_paths['fig5'] = f5_path
    print(f"Generated: {f5_path}")

    return fig_paths


def extract_metrics(df):
    """Serializes key metrics for document inclusion."""
    total_titles = len(df)
    total_movies = int((df['type'] == 'Movie').sum())
    total_tv = int((df['type'] == 'TV Show').sum())
    movie_pct = round((total_movies / total_titles) * 100, 1)
    tv_pct = round((total_tv / total_titles) * 100, 1)

    top_nations = df[df['primary_country'] != 'Unknown']['primary_country'].value_counts().head(5).to_dict()
    mature_share = round((df['rating_bracket'] == 'Adults (18+)').mean() * 100, 1)
    median_movie_len = round(float(df[df['type'] == 'Movie']['movie_duration_min'].median()), 1)
    tv_one_season_pct = round((df[df['type'] == 'TV Show']['tv_seasons_count'] == 1).mean() * 100, 1)

    metrics = {
        'total_titles': total_titles,
        'total_movies': total_movies,
        'total_tv': total_tv,
        'movie_pct': movie_pct,
        'tv_pct': tv_pct,
        'mature_share': mature_share,
        'median_movie_len': median_movie_len,
        'tv_one_season_pct': tv_one_season_pct,
        'top_nations': top_nations
    }

    with open(METRICS_PATH, 'w') as f:
        json.dump(metrics, f, indent=4)

    print(f"Serialized metrics saved to: {METRICS_PATH}")
    return metrics


def main():
    df_raw = acquire_data()
    df_cleaned = clean_and_prepare(df_raw)
    fig_paths = generate_storytelling_visualizations(df_cleaned)
    metrics = extract_metrics(df_cleaned)
    print("\n" + "=" * 60)
    print("NETFLIX DATA STORYTELLING PIPELINE COMPLETED SUCCESSFULLY!")
    print(f"Total Titles: {metrics['total_titles']:,} | Movies: {metrics['movie_pct']}% | TV Shows: {metrics['tv_pct']}%")
    print("=" * 60)


if __name__ == "__main__":
    main()
