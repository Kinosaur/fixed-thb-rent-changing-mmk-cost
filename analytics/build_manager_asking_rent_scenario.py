#!/usr/bin/env python3
"""Create the user-approved same-room asking-rent scenario.

This is a documented scenario, not a reconstructed market-rent history. It
applies the condo manager's annual/period statements to every billing month
within that stated period, as explicitly approved by the user on 2026-08-05.
"""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RECEIPTS = ROOT / "extracted_data" / "interview_abac_monthly_receipts_master.csv"
OUTPUT = ROOT / "data_private" / "manager_asking_rent_monthly_scenario.csv"
TABLEAU_OUTPUT = ROOT / "data_private" / "tableau_rent_comparison_ready.csv"
TABLEAU_DIFFERENCE_OUTPUT = ROOT / "data_private" / "tableau_contract_difference_ready.csv"
FIELDS = [
    "billing_month",
    "new_tenant_asking_rent_thb",
    "scenario_period",
    "scenario_status",
    "scenario_note",
]
TABLEAU_FIELDS = [
    "month_start",
    "rent_type",
    "rent_thb",
    "scenario_period",
]
TABLEAU_DIFFERENCE_FIELDS = [
    "month_start",
    "contract_price_difference_thb",
    "price_status",
    "scenario_period",
]


def scenario_for_month(month: str) -> tuple[int, str, str]:
    if month.startswith("2023-"):
        return (
            6500,
            "2023",
            "User-confirmed same-room contract price; used as the 2023 asking-rent baseline.",
        )
    if month.startswith("2024-"):
        return (
            7000,
            "2024",
            "Manager-reported same-room asking price; user approved applying it to all 2024 billing months.",
        )
    if month.startswith("2025-"):
        return (
            7000,
            "2025",
            "Manager-reported same-room asking price; user approved applying it to all 2025 billing months.",
        )
    if "2026-01" <= month <= "2026-03":
        return (
            7000,
            "2026-01 to 2026-03",
            "Manager-reported same-room asking price before the April 2026 promotion.",
        )
    if month >= "2026-04":
        return (
            6000,
            "2026-04 onward",
            "Manager-reported promotional same-room asking price; user approved applying it from April 2026 onward.",
        )
    raise ValueError(f"No approved asking-rent scenario for {month}")


def main() -> None:
    with RECEIPTS.open(encoding="utf-8", newline="") as file:
        receipt_rows = list(csv.DictReader(file))
    months = [row["billing_month"] for row in receipt_rows]
    if len(months) != len(set(months)):
        raise ValueError("Receipt billing months must be unique before applying the scenario")

    scenario_rows = []
    for month in months:
        rent, period, note = scenario_for_month(month)
        scenario_rows.append({
            "billing_month": month,
            "new_tenant_asking_rent_thb": rent,
            "scenario_period": period,
            "scenario_status": "user_approved_manager_reported_scenario",
            "scenario_note": note,
        })

    tableau_rows = []
    tableau_difference_rows = []
    for row in scenario_rows:
        # January 2023 is a partial receipt period, so keep Tableau aligned with
        # the full-contract comparison query, which starts in February 2023.
        if row["billing_month"] < "2023-02":
            continue
        month_start = f"{row['billing_month']}-01"
        tableau_rows.extend([
            {
                "month_start": month_start,
                "rent_type": "Your fixed contract",
                "rent_thb": 6500,
                "scenario_period": row["scenario_period"],
            },
            {
                "month_start": month_start,
                "rent_type": "New-tenant asking scenario",
                "rent_thb": row["new_tenant_asking_rent_thb"],
                "scenario_period": row["scenario_period"],
            },
        ])
        difference = row["new_tenant_asking_rent_thb"] - 6500
        price_status = (
            "Contract cheaper"
            if difference > 0
            else "Promotion cheaper"
            if difference < 0
            else "Same price"
        )
        tableau_difference_rows.append({
            "month_start": month_start,
            "contract_price_difference_thb": difference,
            "price_status": price_status,
            "scenario_period": row["scenario_period"],
        })

    OUTPUT.parent.mkdir(exist_ok=True)
    with OUTPUT.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(scenario_rows)
    with TABLEAU_OUTPUT.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=TABLEAU_FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(tableau_rows)
    with TABLEAU_DIFFERENCE_OUTPUT.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(
            file, fieldnames=TABLEAU_DIFFERENCE_FIELDS, lineterminator="\n"
        )
        writer.writeheader()
        writer.writerows(tableau_difference_rows)
    print(f"Wrote {len(scenario_rows)} monthly manager-rent scenario rows to {OUTPUT}")
    print(f"Wrote {len(tableau_rows)} Tableau-ready rows to {TABLEAU_OUTPUT}")
    print(
        f"Wrote {len(tableau_difference_rows)} Tableau difference rows to "
        f"{TABLEAU_DIFFERENCE_OUTPUT}"
    )


if __name__ == "__main__":
    main()
