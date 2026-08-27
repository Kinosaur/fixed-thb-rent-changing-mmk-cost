# SQL Queries

These DuckDB practice queries use the project’s local data preparation workflow.

- `01_fixed_contract_sell_baseline.sql` — fixed 6,500 THB rent and total cost in MMK.
- `02_monthly_utilities.sql` — utility-and-other cost and share of monthly THB bill.
- `03_contract_protection_scenario.sql` — fixed contract versus the manager-reported asking-rent scenario.
- `04_monthly_cost_trends.sql` — month-over-month total cost and utility-cost rolling average.

Only queries 2 and 4 run from the public aggregate alone. Queries 1 and 3 use local-only FX or scenario inputs, which are deliberately excluded from Git.

Run a query from the repository root:

```bash
python3 analytics/run_duckdb_query.py sql/02_monthly_utilities.sql
```
