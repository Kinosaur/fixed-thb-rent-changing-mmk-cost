-- First SQL practice: fixed rent and MMK-to-THB Sell-rate exposure.
--
-- Run locally from the repository root in DuckDB. This uses aggregate CSVs
-- only. The source-derived FX monthly summary is intentionally excluded from
-- the first public GitHub milestone while source-use guidance is pending. It
-- does NOT estimate new-tenant rent: that needs comparable-listing evidence
-- from the condo manager or dated listings.

CREATE OR REPLACE VIEW monthly_housing_costs AS
SELECT *
FROM read_csv_auto('data_public/monthly_housing_costs_public.csv');

CREATE OR REPLACE VIEW monthly_myanmar_market_price AS
SELECT *
FROM read_csv_auto('data_public/myanmar_market_price_monthly_summary.csv');

WITH fixed_contract_sell_scenario AS (
    SELECT
        housing.billing_month,
        housing.room_rent_thb AS printed_room_rent_thb,
        6500 AS regular_contract_rent_thb,
        housing.total_housing_cost_thb,
        fx.observation_count AS fx_screenshot_count,
        fx.sell_mmk_per_thb_median,
        ROUND(6500 * fx.sell_mmk_per_thb_median, 2) AS regular_contract_rent_mmk_sell,
        ROUND(
            housing.total_housing_cost_thb * fx.sell_mmk_per_thb_median,
            2
        ) AS total_housing_cost_mmk_sell,
        ROUND(
            (housing.total_housing_cost_thb - 6500) * fx.sell_mmk_per_thb_median,
            2
        ) AS utilities_and_other_cost_mmk_sell
    FROM monthly_housing_costs AS housing
    INNER JOIN monthly_myanmar_market_price AS fx
        ON housing.billing_month = fx.observation_month
    WHERE housing.billing_month >= '2023-02'
)
SELECT *
FROM fixed_contract_sell_scenario
ORDER BY billing_month;

-- Interpretation:
-- * `regular_contract_rent_mmk_sell` is the MMK amount needed for the regular
--   6,500 THB contract rent under the monthly median app Sell rate.
-- * `total_housing_cost_mmk_sell` includes printed utilities and other charges.
-- * `fx_screenshot_count` shows how many source screenshots inform that month.
-- * 2023-01 is intentionally excluded because its printed rent is the
--   non-standard 4,983 THB partial-period value, not the regular 6,500 THB.
