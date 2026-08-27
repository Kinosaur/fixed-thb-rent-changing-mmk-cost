# Public Portfolio Data

`monthly_housing_costs_public.csv` is an anonymized monthly housing-cost summary. It excludes receipt images, names, room number, document number, source filenames, source pages, and notes.

The source-level THB/MMK screenshot table and its monthly summary stay local. The live dashboard uses a documented monthly-median `Sell`-rate scenario and credits [Myanmar Market Price](https://www.myanmarmarketprice.com/); raw observations and screenshots are not part of this repository.

Run `analytics/build_public_portfolio_data.py` locally after updating the private master dataset, then review the resulting public aggregate before sharing.
