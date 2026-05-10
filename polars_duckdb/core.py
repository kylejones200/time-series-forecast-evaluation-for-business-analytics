"""Forecast evaluation metrics using Polars and DuckDB.

MAE, MAPE, sMAPE, MASE are numpy functions in the original. Here they are
replaced by a single DuckDB query — no numpy or sklearn needed for scoring.
"""

import duckdb
import polars as pl
from typing import Dict


def evaluate_forecasts(
    actual: pl.Series,
    predicted: pl.Series,
    training: pl.Series | None = None,
    season: int = 12,
) -> Dict[str, float]:
    """
    Compute MAE, MAPE, sMAPE, and optionally MASE via DuckDB SQL.

    MASE requires the training series to compute the seasonal naive denominator.
    If training is None, MASE is omitted.
    """
    df = pl.DataFrame({"actual": actual, "predicted": predicted})

    base = duckdb.sql("""
        SELECT
            AVG(ABS(actual - predicted))
                AS mae,
            AVG(ABS((actual - predicted) / NULLIF(actual, 0))) * 100
                AS mape,
            AVG(2.0 * ABS(predicted - actual)
                / NULLIF(ABS(actual) + ABS(predicted), 0)) * 100
                AS smape,
            AVG(POWER(actual - predicted, 2))
                AS mse,
            SQRT(AVG(POWER(actual - predicted, 2)))
                AS rmse
        FROM df
    """).pl().row(0, named=True)

    if training is not None and len(training) > season:
        train_df = pl.DataFrame({
            "value":  training,
            "lagged": training.shift(season),
        }).drop_nulls()
        denom = duckdb.sql(
            "SELECT AVG(ABS(value - lagged)) AS d FROM train_df"
        ).pl()[0, "d"]
        base = {**base, "mase": base["mae"] / denom if denom else float("nan")}

    return base


def print_metrics(metrics: Dict[str, float]):
    order = ["mae", "rmse", "mape", "smape", "mase"]
    labels = {"mae": "MAE", "rmse": "RMSE", "mape": "MAPE (%)",
              "smape": "sMAPE (%)", "mase": "MASE"}
    for key in order:
        if key in metrics:
            print(f"  {labels[key]:<12}: {metrics[key]:.4f}")
