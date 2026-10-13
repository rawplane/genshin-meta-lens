# Genshin Impact Meta Data Analysis

A high-performance exploratory and meta-statistical analysis of Genshin Impact characters using modern Python data tooling (**Polars**, **Plotly**, and **Jupyter**).

---

## Executive Summary

This project conducts an empirical meta-analysis of **103** Genshin Impact characters released between 2020 and 2025/2026 across all 7 Teyvat elements, 5 weapon types, and rarity classes (58 5-stars, 45 4-stars).

Instead of relying on subjective community tier lists, this study evaluates character value and meta positioning through objective quantitative indicators:
- **Banner Pull Aggregation**: Total pull counts, average pulls per banner run, and character ubiquity across banner histories.
- **Constellation Retention & Efficiency**: Drop-off rates across C0 to C6/C7, identifying "budget-friendly C0 wonders" versus high-investment "Whale Targets".
- **Stat Powercreep Trajectory**: Multi-year progression of base attributes (Base HP, Base ATK, Base DEF at Level 90) across release versions and years.
- **Role & Element Matrix**: Compositional archetypes (Main DPS, Sub DPS, Support) across elements.

---

## Key Data Insights

### 1. Meta Tier & Pull Analysis
- **4-Star Ubiquity**: Because 4-star rate-ups recur across multiple limited banners, top utility 4-stars exhibit the highest total community pull volumes.
  - **Bennett**: #1 overall pulled character (7,659,164 pulls), highlighting his enduring status as the premiere universal ATK buffer.
  - **Diona** (6.77M pulls), **Yanfei** (6.57M pulls), and **Xingqiu** (6.18M pulls) follow closely.
- **5-Star Ownership**: Standard banner staples (Keqing at 1.34M pulls, Diluc at 1.34M, Jean at 1.34M, Mona at 1.34M) top 5-star lifetime counts due to standard banner off-rate losses, while premier limited supports (e.g. Furina, Nahida, Kazuha) show explosive pulls-per-banner density.

### 2. Constellation Efficiency & Investment Tiers
By evaluating the retention ratio $\frac{\text{C6 pulls}}{\text{C0 pulls}}$, characters are segmented into distinct investment tiers:
- **Whale Targets (High C6 Retention)**:
  - **Chiori**: 21.8% C6/C0 ratio (10,696 C6 pulls vs 49,097 C0 pulls).
  - **Furina**: 16.6% C6/C0 ratio with an unprecedented **60,053 C6 pulls**, showing overwhelming high-constellation investment due to her transformative C6 team heal and DPS conversion.
  - **Arlecchino** (11.2%) and **Mavuika** (10.9%) demonstrate massive C6 pull conversion for hyper-carry DPS units.
- **C0 Budget Staples**:
  - Characters with steep constellation falloffs where C0 unlocks >90% of team utility (e.g., standard buffer/utility units).

### 3. Base Stat Powercreep
Analyzing baseline attributes at Level 90 across release years (2020 to 2025):
- **5-Star Mean ATK**: Risen steadily from **284.8** (2020) to **308.3** (2025), with top offensive characters reaching up to 359 base ATK.
- **Base HP**: Spiked in 2023 with Fontaine's HP-drain/buff meta (averaging 13,704 HP), demonstrating Hoyoverse's regional mechanic-driven stat allocations.
- **Base DEF**: Has trended toward specialized niche scaling (e.g., Geo defense scalers like Chiori and Albedo) rather than uniform inflation.

### 4. Role & Element Distribution
- **Pyro & Cryo**: Heavily skewed toward Main DPS archetypes (Melt/Vaporize core).
- **Hydro & Anemo**: Dominated by Support and Sub DPS roles (Swirl resistance shred, Hydro aura application).
- **Dendro**: Catalyzed reaction-based Sub DPS and Support proliferation post-Version 3.0.

---

## Interactive Notebook

The repository includes an interactive notebook: **`genshin_meta_analysis.ipynb`**.

The notebook comprises 6 structured analytical sections with embedded **Plotly** visualizations:
1. **Dataset Overview & Data Hygiene**: Missing value verification, schema validation, and summary stats.
2. **Pull Volume & Meta Popularity**: Horizontal ranking charts for top 4-star and 5-star pull volumes.
3. **Constellation Efficiency & Whale Thresholds**: Scatter visualization of C0 vs C6 pulls and retention ratios.
4. **Base Stat Powercreep Over Time**: Dual-axis longitudinal trends of HP, ATK, and DEF progression from 2020 to 2025.
5. **Element & Role Archetype Distribution**: Grouped bar charts depicting archetype frequencies across elements.
6. **Executive Meta Conclusions**: Strategic takeaway points for pull planning and meta forecasting.

To generate or rebuild the notebook programmatically:
```bash
python generate_notebook.py
```

---

## Project Structure

```
├── genshin_impact.csv            # Character dataset (103 characters, 31 attributes)
├── analysis.py                   # High-performance Polars ETL & analysis pipeline
├── generate_notebook.py          # Script generating interactive Jupyter notebook
├── genshin_meta_analysis.ipynb   # Generated interactive analysis notebook
├── test_analysis.py              # Unit tests for data processing & metric integrity
├── test_notebook.py              # Structural verification tests for notebook
├── test_readme.py                # Documentation & citation validation tests
└── README.md                     # Comprehensive project documentation & meta report
```

---

## Installation & Setup

### Prerequisites
- Python 3.10+
- Virtual environment tool (`venv`)

### Setup Instructions

1. **Clone repository & initialize environment**:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. **Install dependencies**:
   ```bash
   # Note: polars-lts-cpu is used for maximum compatibility across CPU architectures (including systems without AVX instructions)
   pip install polars-lts-cpu pyarrow plotly nbformat pytest
   ```

3. **Run the Analysis Pipeline & Generate Notebook**:
   ```bash
   python generate_notebook.py
   ```

4. **Run Test Suite**:
   ```bash
   pytest
   ```

5. **Launch Jupyter**:
   ```bash
   jupyter notebook genshin_meta_analysis.ipynb
   ```
