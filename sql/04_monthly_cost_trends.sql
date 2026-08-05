-- Fourth SQL practice: month-over-month cost movement and utility smoothing.
--
-- This public-safe query needs only the anonymized monthly housing summary.
-- The rolling window count makes the first two partial windows visible.

CREATE OR REPLACE VIEW monthly_housing_costs AS
SELECT *
FROM read_csv_auto('data_public/monthly_housing_costs_public.csv');

WITH monthly_costs AS (
    SELECT
        billing_month,
        total_housing_cost_thb,
        total_housing_cost_thb - room_rent_thb AS utilities_and_other_cost_thb
    FROM monthly_housing_costs
),
cost_trends AS (
    SELECT
        billing_month,
        total_housing_cost_thb,
        utilities_and_other_cost_thb,
        total_housing_cost_thb
            - LAG(total_housing_cost_thb) OVER (ORDER BY billing_month)
            AS total_cost_change_from_previous_month_thb,
        ROUND(
            100.0 * (
                total_housing_cost_thb
                - LAG(total_housing_cost_thb) OVER (ORDER BY billing_month)
            )
            / NULLIF(
                LAG(total_housing_cost_thb) OVER (ORDER BY billing_month),
                0
            ),
            1
        ) AS total_cost_change_from_previous_month_pct,
        COUNT(*) OVER (
            ORDER BY billing_month
            ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
        ) AS utility_rolling_window_months,
        ROUND(
            AVG(utilities_and_other_cost_thb) OVER (
                ORDER BY billing_month
                ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
            ),
            2
        ) AS utility_cost_3_month_rolling_avg_thb
    FROM monthly_costs
)
SELECT *
FROM cost_trends
ORDER BY billing_month;

-- Interpretation:
-- * A positive month-over-month value means total printed housing cost rose.
-- * `utility_rolling_window_months` is 1 for the first month and 2 for the
--   second; only 3 indicates a complete three-month average.
-- * The rolling average smooths utility-and-other cost only, not FX or rent.
