# Analytics Scripts

This folder keeps the project reproducible without publishing private evidence.

| Script | Purpose | Input / output boundary |
| --- | --- | --- |
| `build_public_portfolio_data.py` | Builds the anonymized monthly receipt aggregate. | Private master receipts → `data_public/` |
| `build_myanmar_market_price_data.py` | Validates and summarizes supplied FX screenshot observations. | Private screenshots/observations → private summary |
| `build_manager_asking_rent_scenario.py` | Creates the documented asking-rent scenario and Tableau-ready rent comparison. | Private receipt months → private Tableau data |
| `build_tableau_mmk_costs.py` | Creates Tableau-ready MMK cost scenarios. | Public cost aggregate + private FX summary → private Tableau data |
| `build_tableau_cost_composition.py` | Creates the Tableau-ready THB bill composition. | Public aggregate → private Tableau data |
| `run_duckdb_query.py` | Runs a SQL practice query against the local project data. | Local data → terminal output |

The generated Tableau CSV files, source receipts, screenshots, and packaged Tableau workbooks are intentionally excluded by `.gitignore`.

Run the public-safe composition builder with:

```bash
python3 analytics/build_tableau_cost_composition.py
```
