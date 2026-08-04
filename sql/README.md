# SQL Practice

Use DuckDB for this project: it queries CSV files directly and is excellent practice for analytical SQL. Keep the work public-safe—do not load receipt PDFs, screenshots, room number, or source-level identifiers.

Tonight's first query is [01_fixed_contract_sell_baseline.sql](01_fixed_contract_sell_baseline.sql). It joins the public receipt summary to the locally maintained Myanmar Market Price monthly sample, using the user-confirmed `Sell` rate for MMK-to-THB conversion. It produces the regular 6,500 THB contract value in MMK and the full printed housing cost in MMK, without inventing a new-tenant market rent. The source-derived monthly sample is excluded from this first GitHub milestone while source-use guidance is pending, so this query is documented but will not run in a fresh public clone yet.

DuckDB is already available through the local Python environment. Run the query from the repository root:

```bash
python3 analytics/run_duckdb_query.py sql/01_fixed_contract_sell_baseline.sql
```

Then we will add, in order:

1. Utility share, month-over-month change, and a three-month rolling average.
2. A comparable new-tenant asking-rent table once you have manager/listing evidence.
3. The contract-protection calculation in THB and MMK.
