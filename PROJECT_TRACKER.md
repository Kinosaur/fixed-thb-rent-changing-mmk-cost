# Portfolio Project Tracker

## The project in one sentence

Show how a fixed 6,500 THB rent changed in Myanmar-kyat cost over time, then later compare it with evidence-backed new-tenant **asking** rent.

## Active goal

Build a compact, Mac-friendly **data-analyst** portfolio project. It is not a data-science or machine-learning project yet.

## Use these tools — and only these tools for now

| Purpose | Tool | Status |
|---|---|---|
| Query data | DuckDB SQL; DBeaver is optional as the SQL editor | Active |
| Inspect and make a quick chart | Excel for Mac | Active |
| Portfolio visualization | Tableau Public / Tableau Desktop Public Edition on Mac | Next |
| Reproduce analysis | Python + pandas | Later |
| Version control | Git + GitHub | Keep private data excluded |

**Not now:** Power BI Desktop, R, machine learning, Tableau Prep, a cloud database, and a second dashboard tool. Learn one programming language and one visualization tool well before adding another.

## Four learning phases

| Phase | Outcome | Status |
|---|---|---|
| 0. Trusted data | Receipt and FX evidence, definitions, privacy rules | Complete |
| 1. SQL | Four clean queries that answer real housing-cost questions | In progress |
| 2. Tableau | One public-safe, readable interactive story | Ready after Phase 1 |
| 3. Python/pandas | Reproduce the SQL results and one chart in code | Later |
| 4. Portfolio/interview | GitHub case study and a two-minute explanation | Later |

See [the Mac-first learning plan](docs/mac-analytics-learning-plan.md) for the exact tasks.

## Current evidence status

- [x] 43 source-backed receipt months from `2023-01` to `2026-07`.
- [x] 87 dated Myanmar Market Price screenshot observations summarized into 44 monthly values.
- [x] User-confirmed conversion scenario: use the monthly median `Sell` rate for MMK-to-THB cost.
- [x] First SQL query: fixed contract rent expressed in MMK.
- [x] First private Excel chart: monthly median Sell rate.
- [ ] Comparable new-tenant asking rent from manager/listings.
- [ ] Permission or guidance from Myanmar Market Price before publishing any chart based on its rates.

## Data rules that must not change

- A comparable new-tenant figure is an **asking rent**, not a signed market rent, unless a contract proves otherwise.
- The monthly FX figure is the median of available screenshots that month; it is not an official daily rate.
- Keep `source_pdfs/`, `extracted_data/`, `workbook/`, `data_private/`, and screenshots private.
- Never upload personal receipts, screenshots, room number, or source-level evidence to GitHub or Tableau Public.
