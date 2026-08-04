#!/usr/bin/env python3
"""Create a GitHub-safe monthly summary from the private receipt master CSV.

The output deliberately omits room number, document number, source PDF filename,
source page, and review notes. It is suitable for a public portfolio only after
the user reviews the remaining dates and values.
"""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "extracted_data" / "interview_abac_monthly_receipts_master.csv"
OUTPUT = ROOT / "data_public" / "monthly_housing_costs_public.csv"
FIELDS = [
    "billing_month",
    "room_rent_thb",
    "electricity_units",
    "electricity_charge_thb",
    "water_units",
    "water_charge_thb",
    "internet_charge_thb",
    "other_charge_thb",
    "total_housing_cost_thb",
]


def as_number(value: str) -> float:
    return float(value) if value else 0.0


def format_number(value: float) -> int | float:
    return int(value) if value.is_integer() else value


def main() -> None:
    if not INPUT.exists():
        raise FileNotFoundError(f"Private master CSV not found: {INPUT}")
    with INPUT.open(encoding="utf-8", newline="") as input_file:
        source_rows = list(csv.DictReader(input_file))
    output_rows = []
    for row in source_rows:
        output_rows.append({
            "billing_month": row["billing_month"],
            "room_rent_thb": format_number(as_number(row["room_rent_thb"])),
            "electricity_units": format_number(as_number(row["electricity_units_printed"])),
            "electricity_charge_thb": format_number(as_number(row["electricity_charge_thb"])),
            "water_units": format_number(as_number(row["water_units_printed"])),
            "water_charge_thb": format_number(as_number(row["water_charge_thb"])),
            "internet_charge_thb": format_number(as_number(row["internet_charge_thb"])),
            "other_charge_thb": format_number(as_number(row["other_charge_thb"])),
            "total_housing_cost_thb": format_number(as_number(row["printed_grand_total_thb"])),
        })
    OUTPUT.parent.mkdir(exist_ok=True)
    with OUTPUT.open("w", encoding="utf-8", newline="") as output_file:
        writer = csv.DictWriter(
            output_file, fieldnames=FIELDS, lineterminator="\n"
        )
        writer.writeheader()
        writer.writerows(output_rows)
    print(f"Wrote {len(output_rows)} public-safe monthly rows to {OUTPUT}")


if __name__ == "__main__":
    main()
