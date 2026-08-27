# Fixed THB Rent, Changing MMK Cost

An end-to-end personal housing-cost analytics project: receipt evidence was cleaned into monthly aggregates, validated with SQL, and turned into an interactive Tableau dashboard.

**[View the live Tableau Public dashboard](https://public.tableau.com/views/FixedTHBRentChangingMMKCost20232026/Dashboard1)**

## The question

How did a fixed 6,500 THB rent change in Myanmar-kyat terms, what made up the monthly housing bill, and how did the fixed contract compare with a manager-reported same-room asking-rent scenario?

## What the dashboard shows

- The Myanmar-kyat cost of the unchanged 6,500 THB rent over 42 full billing months, from February 2023 to July 2026.
- Monthly housing-bill composition in THB: room rent, electricity, water, internet, and other charges.
- The fixed contract compared with a documented same-room new-tenant asking-rent scenario.

## Methods and boundaries

- The local evidence base contains 43 source-backed receipts from January 2023 to July 2026. January 2023 is a partial first billing period, so the dashboard comparison window starts in February 2023.
- MMK conversion uses the monthly median of available dated `Sell` rates manually transcribed from supplied [Myanmar Market Price](https://www.myanmarmarketprice.com/) screenshots. This is a personal conversion scenario, not an official daily exchange-rate series.
- The asking-rent scenario is manager-reported: 6,500 THB in 2023, 7,000 THB from 2024 through March 2026, and 6,000 THB from April 2026 during a reported promotion. It is not signed market-rent history.
- Receipt images, room information, source-level screenshots, and raw evidence remain local and are never committed.

## Tools

Excel · DuckDB SQL · Tableau Public · Python (data preparation)

## Repository map

- [`data_public/`](data_public/) — reviewed, anonymized monthly aggregates.
- [`analytics/`](analytics/) — repeatable preparation scripts; see its README for data-boundary details.
- [`sql/`](sql/) — four SQL practice queries covering rent, utilities, contract scenario, and trends.
- [`docs/`](docs/) — metric definitions, methodology, and learning notes.
- [`portfolio/`](portfolio/) — the public case-study outline.

## Privacy

The Tableau workbook and all raw evidence are intentionally excluded from Git. Tableau is the public presentation layer; this repository contains code, documentation, and public-safe aggregates only.

## Next step

Reproduce one core SQL result and one dashboard visual in a Python/pandas notebook.
