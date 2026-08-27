# Visualization Plan — Completed Dashboard

The public Tableau dashboard is live: [Fixed THB Rent, Changing MMK Cost](https://public.tableau.com/views/FixedTHBRentChangingMMKCost20232026/Dashboard1).

It contains three connected views:

1. **Monthly cost of fixed 6,500 THB rent (MMK)** — shows the MMK cost of the unchanged rent using the monthly median `Sell` rate.
2. **What made up my monthly housing bill (THB)** — shows room rent, electricity, water, internet, and other charges as monthly stacked bars.
3. **My fixed contract vs new-tenant asking rent (THB)** — compares the fixed contract with the manager-reported same-room asking-rent scenario.

## Interpretation rules

- The MMK series is a personal scenario based on the median of available dated `Sell`-rate screenshots in each month. It is not an official daily-rate series.
- The manager-reported asking-rent scenario is not signed market-rent history.
- The partial January 2023 billing period is excluded from full-month comparisons.
- Do not combine THB and MMK values on one numeric axis.

## Publication boundary

Keep receipt PDFs, screenshots, raw FX observations, room information, and Tableau packages out of Git. The dashboard credits [Myanmar Market Price](https://www.myanmarmarketprice.com/) for the supplied rate screenshots; no response has been received to the courtesy email, so no raw or derived FX table is published here.
