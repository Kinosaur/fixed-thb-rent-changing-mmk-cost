-- Third SQL practice: the fixed-contract versus same-room asking-rent scenario.
--
-- This is a local scenario query. It uses the private monthly manager-rent
-- scenario and the local FX sample, so it will not run in a fresh public clone.
-- The asking-rent schedule is user-approved from manager-reported annual and
-- promotional price statements; it is not a series of observed monthly listings.

CREATE OR REPLACE VIEW monthly_housing_costs AS
SELECT *
FROM read_csv_auto('data_public/monthly_housing_costs_public.csv');

CREATE OR REPLACE VIEW manager_asking_rent_scenario AS
SELECT *
FROM read_csv_auto('data_private/manager_asking_rent_monthly_scenario.csv');

CREATE OR REPLACE VIEW monthly_myanmar_market_price AS
SELECT *
FROM read_csv_auto('data_public/myanmar_market_price_monthly_summary.csv');

WITH contract_protection AS (
    SELECT
        housing.billing_month,
        6500 AS regular_contract_rent_thb,
        scenario.new_tenant_asking_rent_thb,
        scenario.scenario_period,
        scenario.scenario_status,
        scenario.new_tenant_asking_rent_thb - 6500 AS contract_price_difference_thb,
        fx.observation_count AS fx_screenshot_count,
        fx.sell_mmk_per_thb_median,
        ROUND(
            (scenario.new_tenant_asking_rent_thb - 6500)
            * fx.sell_mmk_per_thb_median,
            2
        ) AS contract_price_difference_mmk_sell
    FROM monthly_housing_costs AS housing
    INNER JOIN manager_asking_rent_scenario AS scenario
        ON housing.billing_month = scenario.billing_month
    INNER JOIN monthly_myanmar_market_price AS fx
        ON housing.billing_month = fx.observation_month
    WHERE housing.billing_month >= '2023-02'
)
SELECT *
FROM contract_protection
ORDER BY billing_month;

-- Interpretation:
-- * Positive `contract_price_difference_thb` means the fixed contract cost
--   less than the scenario asking price (contract protection).
-- * Negative values mean the promotional asking price was lower than the
--   fixed contract for that month.
-- * The MMK value converts that THB difference with the monthly median Sell
--   rate. It remains a scenario, not an actual payment or signed-market-rent result.
