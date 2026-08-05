# Bangkok Housing-Cost Analytics Portfolio

Personal housing-cost analytics project for a Bangkok tenant. Exact property details, source receipts, and source-level extraction files remain local and are excluded from Git.

## Portfolio direction

This project is evolving into a public-safe data-analytics and data-science portfolio case study: **Fixed Contract, Floating Currency: Housing-Cost Exposure for a Myanmar Tenant in Bangkok**.

The local analysis compares the regular 6,500 THB contract rent with a user-approved, manager-reported same-room **asking-rent scenario** and expresses selected housing costs in Myanmar kyat using documented exchange-rate scenarios. It does not present that scenario as actual signed-market-rent history. See [PROJECT_TRACKER.md](PROJECT_TRACKER.md) for the learning path and [docs/metric_definitions.md](docs/metric_definitions.md) for the definitions that prevent misleading comparisons.

### Public versus private files

- Keep `source_pdfs/`, `extracted_data/`, `workbook/`, `data_private/`, and `screenshots_mmp_2023-now/` local. They are excluded from Git because they contain source-level or personal evidence.
- Publish only reviewed, anonymized aggregates from `data_public/`, code, templates, documentation, and portfolio visuals with private information removed.
- The public monthly summary is generated with `analytics/build_public_portfolio_data.py`; review it before sharing.

## Current coverage

- Expected coverage: `2023-01` through `2026-07` (43 monthly billing periods).
- Source-backed receipts currently present: 43, covering every expected month from `2023-01` through `2026-07`.
- Four source PDFs provide the evidence: 13 pages for 2023, 11 for 2024, 12 for 2025, and 7 for 2026. Billing months are always derived from `billing_end`, never from the PDF filename.
- No expected billing months are currently missing. No financial values were invented.

## Files

- `source_pdfs/`, `extracted_data/`, `workbook/`, `scripts/extract_receipts.py`, and `extraction_log.md` — private local workflow; excluded from Git.
- `data_public/` — reviewed, anonymous monthly aggregates suitable for portfolio work.
- `data_templates/` — blank templates for comparable rent listings and THB/MMK exchange-rate evidence.
- `analytics/` — reproducible public-safe data preparation code.
- `sql/` — the current practice area. Tableau and Python work begin only in their later phases.
- `PROJECT_TRACKER.md` — the compact Mac-first learning path and project decisions.

## THB/MMK screenshot workflow

The supplied [Myanmar Market Price](https://www.myanmarmarketprice.com/) screenshots are transcribed into a private evidence table and summarized locally by `analytics/build_myanmar_market_price_data.py`. The monthly summary remains out of this initial GitHub milestone while source-use guidance is pending. The documented method uses the median of available dated screenshot observations—not an official daily rate series—and the user-confirmed MMK-to-THB cost scenario uses the app's supplied `Sell` rate. See [the methodology](docs/myanmar_market_price_methodology.md).

## Data rules

- One row represents one receipt. A receipt is identified for duplicate checking by `billing_start`, `billing_end`, `room_number`, and `printed_grand_total_thb`, then confirmed visually against its source page.
- Dates use `YYYY-MM-DD`; `billing_month` uses `YYYY-MM` and is the month containing `billing_end`.
- Raw money and meter fields are numeric. Blank values mean no amount was printed or the value is unavailable; they are not zero. Optional blank charges are treated as zero only in `calculated_grand_total_thb`.
- `document_number` is text, retaining its leading zeros. It is a repeated printed field, not assumed to be a unique receipt ID.
- Source-backed records use `Extracted`, `Verified`, `Needs review`, or `Missing source` as `data_status` values.
- Validation is limited to values printed within the same receipt.
- The manager-rent comparison is a private, user-approved scenario: 6,500 THB in 2023; 7,000 THB from 2024 through March 2026; and a 6,000 THB promotion from April 2026 onward. It is not an observed monthly listing or signed-contract series.

## Calculated validation columns

- `electricity_units_calculated = electricity_meter_end - electricity_meter_start`
- `electricity_units_difference = electricity_units_printed - electricity_units_calculated`
- `electricity_charge_calculated = electricity_units_calculated * electricity_rate_thb`
- `electricity_charge_difference = electricity_charge_thb - electricity_charge_calculated`
- `water_units_calculated = water_meter_end - water_meter_start`
- `water_units_difference = water_units_printed - water_units_calculated`
- `calculated_grand_total_thb = room_rent_thb + electricity_charge_thb + water_charge_thb + internet_charge_thb + other_charge_thb`
- `grand_total_difference = printed_grand_total_thb - calculated_grand_total_thb`

Any non-zero internal difference preserves the printed value and is marked `Needs review`; it is never silently corrected.

## Workbook sheets

1. `Monthly Receipts` — the master receipt table with formula-driven validation columns and Thai-baht formatting.
2. `Review Needed` — automatically lists missing source months and any internal validation exceptions. It excludes cross-receipt meter comparisons.
3. `Validation Summary` — expected versus current coverage, statuses, internal mismatches, duplicates, and factual printed-charge changes.
4. `Data Dictionary` — definitions for every retained field.
5. `Change Log` — important schema and data corrections; it does not log routine formula recalculation.

## Updating for a new source PDF

1. Inspect the existing master CSV and workbook.
2. Visually inspect each new PDF page and extract only readable printed values.
3. Derive `billing_month` from `billing_end` and check for duplicate receipts using the four-field key above.
4. Append only new source-backed records, run the within-receipt calculations, then update the master CSV, workbook, review sheet, validation summary, and change log.
5. Keep any missing months as missing-source findings until a receipt PDF is supplied, and add the source filename to `SOURCE_FILES` when new evidence is added.

To regenerate the current CSV outputs:

```bash
/Users/kaungkhantlin/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 scripts/extract_receipts.py
```
