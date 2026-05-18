# Description: Short example for Time Series Forecast Evaluation for Business Analytics.

import logging

import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)

# Actual and forecast values
actual = np.array([10, 12, 8, 11, 9, 13, 10, 12, 9, 11])
forecast = np.array([9, 11, 10, 12, 8, 14, 9, 11, 10, 10])
# Calculate evaluation metrics
mae = mean_absolute_error(actual, forecast)
rmse = np.sqrt(mean_squared_error(actual, forecast))
logger.info(f"Mean Absolute Error (MAE): {mae:.2f}")
logger.info(f"Root Mean Squared Error (RMSE): {rmse:.2f}")


def mean_absolute_percentage_error(actual, forecast):
    """Compute Mean Absolute Percentage Error (MAPE)"""
    return np.mean(np.abs((actual - forecast) / actual)) * 100


def symmetric_mean_absolute_percentage_error(actual, forecast):
    """Compute Symmetric Mean Absolute Percentage Error (sMAPE)"""
    return np.mean(np.abs(actual - forecast) / ((np.abs(actual) + np.abs(forecast)) / 2)) * 100


def main():
    mape = mean_absolute_percentage_error(actual, forecast)
    smape = symmetric_mean_absolute_percentage_error(actual, forecast)
    logger.info(f"Mean Absolute Percentage Error (MAPE): {mape:.2f}%")
    logger.info(f"Symmetric Mean Absolute Percentage Error (sMAPE): {smape:.2f}%")


if __name__ == "__main__":
    main()
