#!/usr/bin/env python3
"""Validate private THB/MMK observations and create a public monthly sample.

The private input is a manually verified table: one dated historical card from
the Myanmar Market Price app per supplied screenshot.  The public output is a
monthly median of the available screenshot observations, not an official daily
or monthly exchange-rate series.
"""

from __future__ import annotations

import csv
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from statistics import median


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data_private" / "myanmar_market_price_observations.csv"
OUTPUT = ROOT / "data_public" / "myanmar_market_price_monthly_summary.csv"
QUALITY_REPORT = ROOT / "data_private" / "myanmar_market_price_quality_report.md"
REQUIRED_FIELDS = [
    "observation_date",
    "observation_time_bangkok",
    "buy_mmk_per_thb",
    "sell_mmk_per_thb",
    "source_file",
    "source_app",
    "timezone",
    "observation_status",
    "notes",
]
OUTPUT_FIELDS = [
    "observation_month",
    "observation_count",
    "first_observation_date",
    "last_observation_date",
    "buy_mmk_per_thb_median",
    "sell_mmk_per_thb_median",
    "midpoint_mmk_per_thb_median",
    "median_spread_mmk_per_thb",
    "quality_status",
    "coverage_note",
]


def display_number(value: float) -> int | float:
    """Keep whole numbers compact while preserving two-decimal source precision."""
    rounded = round(value, 2)
    return int(rounded) if rounded.is_integer() else rounded


def read_and_validate() -> list[dict[str, object]]:
    if not INPUT.exists():
        raise FileNotFoundError(f"Private FX observations not found: {INPUT}")
    with INPUT.open(encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        if reader.fieldnames != REQUIRED_FIELDS:
            raise ValueError(f"Unexpected input columns: {reader.fieldnames}")
        source_rows = list(reader)

    errors: list[str] = []
    observations: list[dict[str, object]] = []
    source_files: set[str] = set()
    for line_number, row in enumerate(source_rows, start=2):
        if any(not row[field].strip() for field in REQUIRED_FIELDS):
            errors.append(f"Line {line_number}: a required field is blank.")
            continue
        try:
            timestamp = datetime.strptime(
                f"{row['observation_date']} {row['observation_time_bangkok']}",
                "%Y-%m-%d %H:%M",
            )
            buy = float(row["buy_mmk_per_thb"])
            sell = float(row["sell_mmk_per_thb"])
        except ValueError as error:
            errors.append(f"Line {line_number}: invalid date, time, or rate ({error}).")
            continue
        if buy <= 0 or sell <= 0:
            errors.append(f"Line {line_number}: rates must be positive.")
        if buy > sell:
            errors.append(f"Line {line_number}: Buy rate exceeds Sell rate.")
        if row["source_file"] in source_files:
            errors.append(f"Line {line_number}: duplicate source file {row['source_file']}.")
        source_files.add(row["source_file"])
        if row["source_app"] != "Myanmar Market Price":
            errors.append(f"Line {line_number}: unexpected source app.")
        if row["timezone"] != "Asia/Bangkok":
            errors.append(f"Line {line_number}: unexpected timezone.")
        if row["observation_status"] != "verified_from_screenshot":
            errors.append(f"Line {line_number}: unexpected verification status.")
        observations.append({"timestamp": timestamp, "buy": buy, "sell": sell})

    if errors:
        raise ValueError("FX validation failed:\n- " + "\n- ".join(errors))
    if not observations:
        raise ValueError("FX validation failed: no observations were read.")
    return observations


def build_monthly_rows(observations: list[dict[str, object]]) -> list[dict[str, object]]:
    by_month: defaultdict[str, list[dict[str, object]]] = defaultdict(list)
    for observation in observations:
        timestamp = observation["timestamp"]
        assert isinstance(timestamp, datetime)
        by_month[timestamp.strftime("%Y-%m")].append(observation)

    monthly_rows = []
    for month in sorted(by_month):
        rows = sorted(by_month[month], key=lambda item: item["timestamp"])
        buys = [float(item["buy"]) for item in rows]
        sells = [float(item["sell"]) for item in rows]
        midpoints = [(buy + sell) / 2 for buy, sell in zip(buys, sells)]
        spreads = [sell - buy for buy, sell in zip(buys, sells)]
        first = rows[0]["timestamp"]
        last = rows[-1]["timestamp"]
        assert isinstance(first, datetime) and isinstance(last, datetime)
        monthly_rows.append({
            "observation_month": month,
            "observation_count": len(rows),
            "first_observation_date": first.strftime("%Y-%m-%d"),
            "last_observation_date": last.strftime("%Y-%m-%d"),
            "buy_mmk_per_thb_median": display_number(median(buys)),
            "sell_mmk_per_thb_median": display_number(median(sells)),
            "midpoint_mmk_per_thb_median": display_number(median(midpoints)),
            "median_spread_mmk_per_thb": display_number(median(spreads)),
            "quality_status": "sampled_screenshot_observations",
            "coverage_note": "Median of supplied dated history screenshots; not an official or daily rate series.",
        })
    return monthly_rows


def write_quality_report(observations: list[dict[str, object]], monthly_rows: list[dict[str, object]]) -> None:
    dates = sorted(item["timestamp"] for item in observations)
    assert all(isinstance(item, datetime) for item in dates)
    report = "\n".join([
        "# Myanmar Market Price Data-Quality Report",
        "",
        f"- Source screenshot observations: {len(observations)}",
        f"- Distinct calendar months: {len(monthly_rows)}",
        f"- First dated observation: {dates[0].strftime('%Y-%m-%d %H:%M')} Asia/Bangkok",
        f"- Last dated observation: {dates[-1].strftime('%Y-%m-%d %H:%M')} Asia/Bangkok",
        "- Validation passed: required fields, parseable dates/times, positive rates, Buy <= Sell, unique source filenames, expected app, timezone, and verification status.",
        "- Limitation: observations are manually transcribed samples from supplied screenshots. They are not an official, complete daily FX time series and must not be forward-filled.",
        "",
    ])
    QUALITY_REPORT.parent.mkdir(exist_ok=True)
    QUALITY_REPORT.write_text(report, encoding="utf-8")


def main() -> None:
    observations = read_and_validate()
    monthly_rows = build_monthly_rows(observations)
    OUTPUT.parent.mkdir(exist_ok=True)
    with OUTPUT.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=OUTPUT_FIELDS)
        writer.writeheader()
        writer.writerows(monthly_rows)
    write_quality_report(observations, monthly_rows)
    print(f"Validated {len(observations)} private screenshot observations.")
    print(f"Wrote {len(monthly_rows)} public monthly rows to {OUTPUT}")
    print(f"Wrote data-quality report to {QUALITY_REPORT}")


if __name__ == "__main__":
    main()
