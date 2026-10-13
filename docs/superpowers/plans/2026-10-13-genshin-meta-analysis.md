# Genshin Impact Meta Analysis Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Perform an end-to-end meta analysis of Genshin Impact character data (pull rates, constellation investments, role/element ecosystems, stat scaling) using modern Python data tooling (Polars, Plotly), producing an interactive Jupyter Notebook and comprehensive README.md.

**Architecture:** Use Polars for efficient DataFrame parsing, feature engineering, and statistical aggregations. Write modular data pipeline and validation functions in Python, embed structured analysis and visualizations into `genshin_meta_analysis.ipynb`, and document business insights in `README.md`.

**Tech Stack:** Python 3.12+, Polars, Plotly, nbformat, pytest.

**Spec:** Local dataset `genshin_impact.csv` (103 characters, 31 columns).

## Global Constraints

- Use Polars (`polars`) as the primary DataFrame manipulation library.
- Use Plotly (`plotly.graph_objects` / `plotly.express`) for rich, modern visualizations.
- Python code must execute cleanly within `.venv`.
- Deliverables required: `analysis.py` (core reusable pipeline), `test_analysis.py` (unit checks), `genshin_meta_analysis.ipynb` (clean valid notebook), and `README.md`.

## Review Focus

- Correct string parsing of array columns `banner_versions` and `banner_dates`.
- Proper handling of comma-separated roles (`roles`) across multiple category splits.
- Division-by-zero safety when calculating rates (e.g. `pulled_count / num_banners` where num_banners > 0).
- Constellation pull retention calculation consistency (C0 vs C1..C6 pulls).
- Valid Jupyter notebook structure conforming to nbformat v4 specification.

---

### Task 1: Core Data Pipeline and Meta Metric Aggregations

**Files:**
- Create: `analysis.py`
- Test: `test_analysis.py`

**Interfaces:**
- Produces:
  - `load_and_clean_data(csv_path: str) -> polars.DataFrame`
  - `compute_pull_meta(df: polars.DataFrame) -> polars.DataFrame`
  - `compute_constellation_efficiency(df: polars.DataFrame) -> polars.DataFrame`
  - `compute_role_element_matrix(df: polars.DataFrame) -> polars.DataFrame`
  - `compute_stat_powercreep(df: polars.DataFrame) -> polars.DataFrame`

- [ ] **Step 1: Write test cases for data cleaning and metrics in `test_analysis.py`**
- [ ] **Step 2: Run pytest to verify test failures**
- [ ] **Step 3: Implement functions in `analysis.py`**
- [ ] **Step 4: Run pytest to verify all tests pass**
- [ ] **Step 5: Commit changes**

---

### Task 2: Interactive Analysis Notebook Generation

**Files:**
- Create: `generate_notebook.py`
- Create: `genshin_meta_analysis.ipynb`

**Interfaces:**
- Consumes: `analysis.py` pipeline functions
- Produces: `genshin_meta_analysis.ipynb` containing 6 rich sections with markdown analysis, code cells, and Plotly interactive charts.

- [ ] **Step 1: Write notebook generator script `generate_notebook.py` utilizing `nbformat`**
- [ ] **Step 2: Run generator to output `genshin_meta_analysis.ipynb`**
- [ ] **Step 3: Execute notebook verification via python to ensure syntax and structure validity**
- [ ] **Step 4: Commit changes**

---

### Task 3: Comprehensive Meta Documentation and Project README

**Files:**
- Create: `README.md`

**Interfaces:**
- Consumes: Findings and summaries from `analysis.py` and `genshin_meta_analysis.ipynb`
- Produces: `README.md` with executive summary, meta tier insights, constellation guide, and execution steps.

- [ ] **Step 1: Draft executive summary and data findings in `README.md`**
- [ ] **Step 2: Verify formatting, metrics citations, and environment instructions**
- [ ] **Step 3: Commit changes**
