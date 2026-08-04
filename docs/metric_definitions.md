# Metric Definitions

## Contract rent

The printed monthly room-rent charge. The normal baseline is 6,500 THB from `2023-02` onward. The `2023-01` receipt is retained as printed because its room rent is 4,983 THB and should not be silently replaced.

## Comparable new-tenant asking rent

The median `listed_rent_thb` among listings marked `Comparable` for the selected market snapshot. A listing should ideally match the building, room type, size, furnishing level, and contract term. This metric represents an advertised asking price, not a completed lease, unless a signed rent is independently documented.

## Contract-rent saving

`comparable_asking_rent_median_thb - contract_rent_thb`

A positive result means the comparable new-tenant asking-rent median is above the contract rent.

## Total housing cost

`room_rent_thb + electricity_charge_thb + water_charge_thb + internet_charge_thb + other_charge_thb`

Use the printed receipt charges, not inferred utility rates.

## Kyat housing cost

`total_housing_cost_thb × mmk_per_thb`

Every kyat result must state its rate source, rate date, and `rate_basis`: `reference`, `remittance_market`, or `actual_payment`. Do not combine these rate bases into one series.

## Myanmar Market Price screenshot scenarios

For the supplied screenshot sample, retain both source labels: `Buy (MMK)` and `Sell (MMK)`. The user has confirmed that their MMK-to-THB transaction uses the app's `Sell` rate, so the primary personal-cost scenario uses `sell_mmk_per_thb_median`. Keep `Buy` available for source transparency and do not treat it as the user's paid-cost scenario.

The public monthly file is a median of the available dated screenshot observations. It is a sampled market series rather than an official or complete daily FX series; use its sample count and coverage dates in any chart or conclusion.
