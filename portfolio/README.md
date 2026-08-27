# Portfolio Case Study

## Fixed THB Rent, Changing MMK Cost

**[Live Tableau dashboard](https://public.tableau.com/views/FixedTHBRentChangingMMKCost20232026/Dashboard1)**

### Business question

How can a fixed Thai-baht housing contract still become less affordable for a Myanmar tenant, and when does that contract protect against a new-tenant asking-rent scenario?

### Approach

1. Extracted and validated 43 monthly rental receipts.
2. Created public-safe monthly cost aggregates.
3. Used the monthly median of supplied Myanmar Market Price `Sell`-rate screenshots for a documented MMK conversion scenario.
4. Modeled a manager-reported same-room asking-rent scenario separately from signed market rent.
5. Built an interactive Tableau dashboard covering February 2023 to July 2026, excluding the partial first billing period.

### Dashboard story

- A fixed 6,500 THB rent did not create a fixed MMK obligation.
- Electricity was the largest changing component above rent in the monthly THB bill.
- The contract was cheaper than the asking-rent scenario through March 2026; a reported April 2026 promotion reversed that comparison.

### Limitations

- The THB/MMK series is not an official or complete daily exchange-rate series.
- New-tenant values are manager-reported asking-rent scenarios, not signed contracts or a market-wide rental index.
- The dashboard uses anonymized, single-tenant housing-cost data and should not be generalized to all Bangkok tenants.

### Skills demonstrated

Data cleaning · validation · SQL · scenario analysis · Tableau dashboard design · source attribution · privacy-aware portfolio publishing

Never include unredacted receipts, names, room number, document numbers, bank details, or private screenshots in this folder.
