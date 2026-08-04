#!/usr/bin/env python3
"""Run a local DuckDB SQL file and print the final result as CSV.

Usage:
    python3 analytics/run_duckdb_query.py sql/01_fixed_contract_sell_baseline.sql
"""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

import duckdb


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("sql_file", type=Path, help="SQL file to run from the repository root")
    args = parser.parse_args()

    if not args.sql_file.is_file():
        raise FileNotFoundError(f"SQL file not found: {args.sql_file}")

    result = duckdb.connect().execute(args.sql_file.read_text(encoding="utf-8"))
    if result.description is None:
        print("SQL completed; the file did not return rows.")
        return

    writer = csv.writer(sys.stdout)
    writer.writerow([column[0] for column in result.description])
    writer.writerows(result.fetchall())


if __name__ == "__main__":
    main()
