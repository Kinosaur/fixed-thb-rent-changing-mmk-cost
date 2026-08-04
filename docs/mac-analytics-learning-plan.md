# Plan: Mac Data Analytics Learning

**Generated:** 2026-08-04
**Estimated complexity:** Low, if completed one small task at a time.

## Overview

This is a personal portfolio project for entry-level data-analyst roles in Thailand or Taiwan. The durable skills to show are SQL, spreadsheet judgment, data visualization, Python, and clear communication. The project does not need Power BI Desktop, R, machine learning, or several dashboard tools.

## Assumptions and non-goals

- Target: entry-level data analyst / BI analyst path, with data-science skills added later.
- Device: MacBook.
- Current priority: protect time during exams and classes.
- Non-goals: predict rent prices, predict exchange rates, or claim a full official FX history.

## Keep, pause, and do not publish

### Keep

- `extracted_data/`, source PDFs, and the receipt workbook as private evidence.
- `data_public/` as the only source for future public charts.
- The FX methodology, SQL query, private Excel chart, and README.

### Pause

- `power_bi/`: do not learn or build Power BI Desktop artifacts on this Mac.
- `notebooks/` and `requirements-python-phase.txt`: wait until Phase 3.
- Extra templates and scripts unless a current phase uses them.

### Never publish

- Receipt PDFs, screenshots, room number, document numbers, or raw screenshot observations.
- Any Tableau Public workbook before the data inside is confirmed public-safe. Tableau Public workbooks and their data are public and downloadable.

## Phase 1: SQL — four useful queries

**Goal:** answer four housing-cost questions in SQL before opening Tableau.

**Demo/validation:** each query runs in DuckDB and uses only `data_public/` CSVs.

1. **Fixed contract cost in MMK** — already complete in `sql/01_fixed_contract_sell_baseline.sql`.
2. **Monthly utilities** — calculate `total_housing_cost_thb - room_rent_thb` and its percentage of the total.
3. **Month-over-month change** — show whether the full housing cost in THB rose or fell from the previous month.
4. **Three-month rolling average** — smooth utility cost only, not the FX rate or market rent.

Stop after these four. They demonstrate joins, calculations, `LAG`, and window functions.

## Phase 2: Tableau — one story, not a dashboard collection

**Goal:** create one Tableau workbook with two or three related views.

**Demo/validation:** every chart has a title, unit, source note, and no private data.

1. Rebuild the monthly MMP Sell-rate trend from `data_public/myanmar_market_price_monthly_summary.csv`.
2. Build the fixed 6,500 THB rent in MMK from the SQL output.
3. Build total housing cost in MMK versus rent-only MMK.
4. Add the comparable asking-rent chart only after manager/listing evidence arrives.

Use Tableau Public as a local learning tool first. Publish only after Myanmar Market Price responds or you choose a chart that contains no MMP-derived values.

## Phase 3: Python and pandas — reproduce, do not restart

**Goal:** turn the existing manual/SQL analysis into a repeatable script or notebook.

**Demo/validation:** Python output matches a selected SQL result and has checks for duplicate months, missing rates, and invalid rates.

1. Read the two public CSVs with pandas.
2. Join monthly housing costs to the Sell-rate summary.
3. Reproduce the contract-rent MMK calculation.
4. Generate one clean matplotlib chart with the same source note.

Use Python first. Add R only if a class assignment or a target job makes it necessary.

## Phase 4: Portfolio and interview

**Goal:** publish one careful case study, not every working file.

**Demo/validation:** a reader can answer “what was the question, what data was used, what did you do, what did you find, and what are the limits?” in under two minutes.

1. Publish public-safe CSVs, SQL, Python, methodology, and final visuals.
2. Write a short case-study README.
3. Practise explaining: “The THB contract was fixed, but its MMK cost changed with the Sell rate.”
4. Add the market-rent scenario only when its evidence is ready.

## Weekly rhythm during exam periods

- One 30-minute SQL task, once or twice per week.
- One 30-minute Tableau or Python task after a SQL query is understood.
- Stop at the time limit. Consistency matters more than a large dashboard.

## Potential risks and mitigations

- **Too many tools:** keep SQL + Tableau + Python; do not learn R or Power BI now.
- **Privacy:** test every public file against `.gitignore`; never use raw evidence in a public visual.
- **FX source rights:** wait for Myanmar Market Price’s reply before publishing MMP-based charts; keep practising locally meanwhile.
- **Taiwan/Thailand job search:** tools are only one part of readiness. Language, visa/work authorization, communication, and domain experience can matter as much as the tool list.
