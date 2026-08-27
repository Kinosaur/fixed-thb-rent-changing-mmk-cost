#!/usr/bin/env python3
"""Create a simple Tableau-ready view of fixed Thai-baht costs in MMK."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HOUSING = ROOT / "data_public" / "monthly_housing_costs_public.csv"
FX = ROOT / "data_public" / "myanmar_market_price_monthly_summary.csv"
OUTPUT = ROOT / "data_private" / "tableau_mmk_costs_ready.csv"
COMPARISON_OUTPUT = ROOT / "data_private" / "tableau_mmk_cost_comparison_ready.csv"
FIELDS = [
    "month_start",
    "fixed_contract_rent_mmk_sell",
    "total_housing_cost_mmk_sell",
    "sell_mmk_per_thb_median",
    "fx_screenshot_count",
]
COMPARISON_FIELDS = [
    "month_start",
    "cost_type",
    "cost_mmk",
    "sell_mmk_per_thb_median",
    "fx_screenshot_count",
]


def main() -> None:
    with HOUSING.open(encoding="utf-8", newline="") as file:
        housing_rows = list(csv.DictReader(file))
    with FX.open(encoding="utf-8", newline="") as file:
        fx_by_month = {
            row["observation_month"]: row
            for row in csv.DictReader(file)
        }

    output_rows = []
    comparison_rows = []
    for housing in housing_rows:
        month = housing["billing_month"]
        if month < "2023-02":
            continue
        fx = fx_by_month.get(month)
        if fx is None:
            raise ValueError(f"No FX sample available for {month}")
        sell_rate = float(fx["sell_mmk_per_thb_median"])
        row = {
            "month_start": f"{month}-01",
            "fixed_contract_rent_mmk_sell": round(6500 * sell_rate, 2),
            "total_housing_cost_mmk_sell": round(
                float(housing["total_housing_cost_thb"]) * sell_rate, 2
            ),
            "sell_mmk_per_thb_median": sell_rate,
            "fx_screenshot_count": int(fx["observation_count"]),
        }
        output_rows.append(row)
        comparison_rows.extend([
            {
                "month_start": row["month_start"],
                "cost_type": "Fixed 6,500 THB rent",
                "cost_mmk": row["fixed_contract_rent_mmk_sell"],
                "sell_mmk_per_thb_median": sell_rate,
                "fx_screenshot_count": row["fx_screenshot_count"],
            },
            {
                "month_start": row["month_start"],
                "cost_type": "Total housing cost",
                "cost_mmk": row["total_housing_cost_mmk_sell"],
                "sell_mmk_per_thb_median": sell_rate,
                "fx_screenshot_count": row["fx_screenshot_count"],
            },
        ])

    OUTPUT.parent.mkdir(exist_ok=True)
    with OUTPUT.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(output_rows)
    with COMPARISON_OUTPUT.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=COMPARISON_FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(comparison_rows)
    print(f"Wrote {len(output_rows)} Tableau-ready MMK cost rows to {OUTPUT}")
    print(
        f"Wrote {len(comparison_rows)} Tableau-ready comparison rows "
        f"to {COMPARISON_OUTPUT}"
    )


if __name__ == "__main__":
    main()
