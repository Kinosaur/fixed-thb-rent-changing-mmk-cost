# Myanmar Market Price THB/MMK Methodology

## Purpose

This dataset supports a personal housing-cost scenario analysis for a Myanmar tenant in Bangkok. It records the Thai-baht to Myanmar-kyat rates displayed by the supplied **Myanmar Market Price** app screenshots, then derives a public-safe monthly sample for analysis.

## Source and grain

- Source: 87 supplied PNG screenshots from the [Myanmar Market Price](https://www.myanmarmarketprice.com/) app and website.
- One private-table row equals one screenshot and one dated **Changes History** card.
- The app labels the unit as `THB 1 ฿` and the rates as `Buy (MMK)` and `Sell (MMK)`; those source labels are retained without reinterpretation.
- Dates and times are taken from the app and use `Asia/Bangkok (UTC+07:00)`.
- The source filenames and screenshots remain private. `IMG_1104.PNG` was not supplied; no value was created for it.

## Source credit

Exchange-rate observations are attributed to [Myanmar Market Price](https://www.myanmarmarketprice.com/). The project manually transcribes only the dated values visible in user-supplied app screenshots for personal analysis. This attribution does not imply affiliation with, endorsement by, or an official data partnership with Myanmar Market Price.

## Extraction rule

For every screenshot, the first fully dated historical card in **Changes History** was transcribed. The top **Latest Price** panel was deliberately excluded: it is a current app value at screenshot capture, not the historical rate for the visible card date.

## Validation

`analytics/build_myanmar_market_price_data.py` validates all required fields, parses dates and times, requires positive rates, checks `Buy <= Sell`, checks each source filename is unique, and confirms the expected app, timezone, and verification status. It writes a private data-quality report and a public monthly summary.

## Public monthly summary

`data_public/myanmar_market_price_monthly_summary.csv` contains the median of the available screenshot observations in each calendar month. It reports the observed-date range and sample count. The midpoint is calculated within each observation as `(Buy + Sell) / 2`, then summarized with the median; it is descriptive only.

Months with no supplied screenshots remain absent. Rates are never forward-filled, interpolated, averaged with a different source, or presented as an official reference series.

## Critical interpretation decision

The app's `Buy` and `Sell` labels do not by themselves establish which rate represents the user's actual cost of obtaining baht. Before calculating a personal MMK burden, confirm with the exchange provider which side applies to the transaction. Until then, analyses should show both Buy and Sell scenarios rather than selecting one as the truth.

## Limitations

- This is a manually transcribed, user-supplied screenshot sample, not a complete daily time series.
- Screenshot density varies by month, so a monthly median describes only the observed samples.
- It should not be used to forecast kyat, assert an official rate, or claim a transfer rate the user did not actually receive.
