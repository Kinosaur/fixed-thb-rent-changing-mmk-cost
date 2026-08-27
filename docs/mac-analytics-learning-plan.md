# Mac-First Analytics Learning Plan

This project is a compact entry-level analyst portfolio piece. The objective is to show sound data judgment, reproducible analysis, and clear communication—not to use every analytics tool.

## Completed

- **Trusted data:** 43 receipt-backed monthly records were cleaned and validated locally.
- **SQL:** DuckDB queries answer utility-cost, contract-scenario, and monthly-trend questions.
- **Tableau:** a three-view public dashboard is live on [Tableau Public](https://public.tableau.com/views/FixedTHBRentChangingMMKCost20232026/Dashboard1).

## Next: Python and pandas

Reproduce one existing result instead of creating a new analysis.

1. Create a notebook that reads `data_public/monthly_housing_costs_public.csv`.
2. Validate unique billing months and numeric cost fields.
3. Recreate monthly utilities: total housing cost minus room rent.
4. Produce one chart and compare its values with the equivalent SQL query.
5. Explain the result and its limitations in the notebook.

## Tools to use now

| Purpose | Tool |
|---|---|
| Query and analytical thinking | DuckDB SQL |
| Dashboard and communication | Tableau Public |
| Reproducible analysis | Python + pandas |
| Version control and case study | GitHub |

Do not add Power BI Desktop on this Mac. Add R only if a course or job target requires it.

## Privacy rule

Never publish receipt PDFs, source screenshots, room details, raw exchange-rate observations, or Tableau packages. Keep public work limited to reviewed aggregates, code, documentation, and the live dashboard.
