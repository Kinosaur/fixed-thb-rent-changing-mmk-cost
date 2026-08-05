# Visualization Plan

## What can be visualized now

The receipt data, Myanmar Market Price screenshot sample, and user-approved manager-rent scenario are sufficient for five honest charts. They answer how the same fixed Thai-baht contract changed in Myanmar-kyat terms and compare it with a manager-reported same-room asking-rent scenario.

### Chart 1 — THB/MMK Sell rate over time

- **Chart type:** line chart with monthly points.
- **X-axis:** `observation_month`.
- **Y-axis:** `sell_mmk_per_thb_median` (MMK per 1 THB).
- **Source file:** `data_public/myanmar_market_price_monthly_summary.csv`.
- **Purpose:** show the monthly median rate used for the user's MMK-to-THB conversion.

### Chart 2 — Fixed 6,500 THB rent expressed in MMK

- **Chart type:** line chart with monthly points.
- **X-axis:** `billing_month`.
- **Y-axis:** `regular_contract_rent_mmk_sell`.
- **Source:** output of `sql/01_fixed_contract_sell_baseline.sql`.
- **Purpose:** show how the MMK cost of the unchanged 6,500 THB rent changed with the Sell rate.

### Chart 3 — Rent-only versus total monthly housing cost in MMK

- **Chart type:** two-line chart.
- **X-axis:** `billing_month`.
- **Y-axis:** MMK.
- **Series:** `regular_contract_rent_mmk_sell` and `total_housing_cost_mmk_sell`.
- **Purpose:** separate currency exposure from utilities and other receipt charges.

## Required chart note

Add this as a subtitle or footnote to every FX chart:

> Source: Myanmar Market Price. Values were manually transcribed from user-supplied dated app screenshots and summarized as the median of available observations in each month. Sell rate used for the user's MMK-to-THB cost scenario. Not an official or complete daily-rate series.

Also include `fx_screenshot_count` in an adjacent table or chart tooltip. A count of 1 means only one screenshot informed that month's median; it does not mean the rate is wrong.

## Manager-rent scenario rules

- Use a step line, not a smooth trend line: 6,500 THB in 2023; 7,000 THB from 2024 through March 2026; 6,000 THB from April 2026 onward.
- Label it **Manager-reported same-room asking-rent scenario**.
- Do not call it actual market rent, an observed monthly listing series, or a signed-contract series.

## Do not do these

- Do not put THB and MMK on the same numeric axis; they are different units.
- Do not use the app's top Latest Price as a historical observation.
- Do not use a smoothed or forecast rate.

## Manager-rent comparison charts

Add Chart 4: 6,500 THB contract rent versus the manager-reported same-room asking-rent scenario in THB. Then add Chart 5: contract price difference in MMK using the same monthly median Sell-rate method. Label it **manager-reported asking-rent scenario**, not actual signed market rent.

## Publication boundary

Keep screenshots, raw observations, and personal receipt records private. Before publishing a GitHub chart that uses the Myanmar Market Price sample, send a short permission/courtesy email and follow any requested attribution or use conditions.
