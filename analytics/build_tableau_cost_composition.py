#!/usr/bin/env python3
"""Create a Tableau-ready monthly THB housing-cost composition view."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data_public" / "monthly_housing_costs_public.csv"
OUTPUT = ROOT / "data_private" / "tableau_cost_composition_thb_ready.csv"

COMPONENTS = (
    ("Room rent", "room_rent_thb"),
    ("Electricity", "electricity_charge_thb"),
    ("Water", "water_charge_thb"),
    ("Internet", "internet_charge_thb"),
    ("Other", "other_charge_thb"),
)
FIELDS = ("month_start", "cost_component", "cost_thb")


def main() -> None:
    with SOURCE.open(encoding="utf-8", newline="") as file:
        source_rows = list(csv.DictReader(file))

    output_rows = []
    for source_row in source_rows:
        month = source_row["billing_month"]
        # January 2023 is a partial first billing period, so exclude it from
        # monthly full-bill comparisons and align this view with the FX series.
        if month < "2023-02":
            continue

        component_total = sum(float(source_row[field]) for _, field in COMPONENTS)
        receipt_total = float(source_row["total_housing_cost_thb"])
        if round(component_total, 2) != round(receipt_total, 2):
            raise ValueError(
                f"Component total does not reconcile for {month}: "
                f"{component_total} != {receipt_total}"
            )

        for label, field in COMPONENTS:
            output_rows.append(
                {
                    "month_start": f"{month}-01",
                    "cost_component": label,
                    "cost_thb": source_row[field],
                }
            )

    OUTPUT.parent.mkdir(exist_ok=True)
    with OUTPUT.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(output_rows)

    print(f"Wrote {len(output_rows)} component rows to {OUTPUT}")


if __name__ == "__main__":
    main()
