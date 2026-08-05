-- Second SQL practice: monthly utilities and utility share in THB.
--
-- This query uses only the public-safe housing summary. Unlike the FX query,
-- it works in a fresh clone because it needs no private source-derived data.

CREATE OR REPLACE VIEW monthly_housing_costs AS
SELECT *
FROM read_csv_auto('data_public/monthly_housing_costs_public.csv');

SELECT
    billing_month,
    room_rent_thb,
    total_housing_cost_thb,
    total_housing_cost_thb - room_rent_thb AS utilities_and_other_cost_thb,
    ROUND(
        100.0 * (total_housing_cost_thb - room_rent_thb)
        / NULLIF(total_housing_cost_thb, 0),
        1
    ) AS utility_share_pct
FROM monthly_housing_costs
ORDER BY billing_month;

-- Interpretation:
-- * `utilities_and_other_cost_thb` includes electricity, water, internet,
--   and other printed charges.
-- * `utility_share_pct` is the percentage of the printed total that was not
--   the room-rent charge. It is a percentage of total housing cost, not rent.
