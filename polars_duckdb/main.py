#!/usr/bin/env python3
"""Forecast evaluation — Polars + DuckDB rewrite (no sklearn, no numpy metrics)."""

import sys
import logging
import numpy as np
import polars as pl
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from core import evaluate_forecasts, print_metrics

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
OUTPUT_DIR = Path(__file__).parent.parent / "images"
OUTPUT_DIR.mkdir(exist_ok=True)


def make_synthetic(n: int = 120, season: int = 12, seed: int = 42):
    """Seasonal series split into train / test with a naive seasonal forecast."""
    rng = np.random.default_rng(seed)
    t = np.arange(n)
    signal = 1000 + 50 * np.sin(2 * np.pi * t / season) + rng.normal(0, 20, n)

    train_n = n - season
    train = pl.Series("value", signal[:train_n].tolist())
    actual = pl.Series("actual", signal[train_n:].tolist())

    # naive seasonal forecast: repeat the last season of training data
    naive = pl.Series("predicted", signal[train_n - season: train_n].tolist())

    return train, actual, naive


def main():
    train, actual, naive = make_synthetic()

    logging.info("=== Naive seasonal forecast metrics ===")
    metrics = evaluate_forecasts(actual, naive, training=train, season=12)
    print_metrics(metrics)

    # Compare against a slightly better (trend-adjusted) forecast
    noise = np.random.default_rng(99).normal(0, 10, len(actual))
    better = pl.Series("predicted", (actual.to_numpy() + noise).tolist())

    logging.info("\n=== Trend-adjusted forecast metrics ===")
    metrics2 = evaluate_forecasts(actual, better, training=train, season=12)
    print_metrics(metrics2)

    logging.info(f"\nDone. Outputs in {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
