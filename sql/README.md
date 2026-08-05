# SQL Practice

Use DuckDB for this project: it queries CSV files directly and is excellent practice for analytical SQL. Keep the work public-safe—do not load receipt PDFs, screenshots, room number, or source-level identifiers.

Tonight's first query is [01_fixed_contract_sell_baseline.sql](01_fixed_contract_sell_baseline.sql). It joins the public receipt summary to the locally maintained Myanmar Market Price monthly sample, using the user-confirmed `Sell` rate for MMK-to-THB conversion. It produces the regular 6,500 THB contract value in MMK and the full printed housing cost in MMK, without inventing a new-tenant market rent. The source-derived monthly sample is excluded from this first GitHub milestone while source-use guidance is pending, so this query is documented but will not run in a fresh public clone yet.

The second query, [02_monthly_utilities.sql](02_monthly_utilities.sql), needs only the public-safe housing summary. It calculates the Thai-baht utility-and-other cost and its share of total housing cost for every receipt month.

The third query, [03_contract_protection_scenario.sql](03_contract_protection_scenario.sql), compares the fixed 6,500 THB contract with the user-approved, manager-reported same-room asking-rent scenario. It shows the price difference in THB and in MMK using the monthly median Sell rate. Both its rent scenario and FX source stay local.

The fourth query, [04_monthly_cost_trends.sql](04_monthly_cost_trends.sql), is public-safe. It calculates month-over-month total-cost movement and a three-month rolling average of utility-and-other cost, with a visible window count for the first two partial averages.

DuckDB is already available through the local Python environment. Run the query from the repository root:

```bash
python3 analytics/run_duckdb_query.py sql/01_fixed_contract_sell_baseline.sql

python3 analytics/run_duckdb_query.py sql/02_monthly_utilities.sql

python3 analytics/build_manager_asking_rent_scenario.py
python3 analytics/run_duckdb_query.py sql/03_contract_protection_scenario.sql

python3 analytics/run_duckdb_query.py sql/04_monthly_cost_trends.sql
```

These four queries complete the SQL practice phase. Next: build the Tableau story from their outputs.
