"""Evaluation metrics for ML models.

TODO: sentiment — accuracy, macro-F1, per-class precision/recall.
TODO: forecast — MAE, RMSE, directional accuracy, interval coverage.
TODO: risk — MAE/RMSE vs labels when defined.
TODO: anomaly — precision on labeled events when available.
"""

from __future__ import annotations

from typing import Any


def evaluate_sentiment(y_true: Any, y_pred: Any) -> dict[str, Any]:
    """TODO: accuracy, macro-F1, per-class precision/recall."""
    raise NotImplementedError("TODO: implement sentiment metrics")


def evaluate_forecast(y_true: Any, y_pred: Any, intervals: Any = None) -> dict[str, Any]:
    """TODO: MAE, RMSE, directional accuracy, interval coverage."""
    raise NotImplementedError("TODO: implement forecast metrics")


def evaluate_risk(y_true: Any, y_pred: Any) -> dict[str, Any]:
    """TODO: MAE/RMSE vs labeled risk when the team defines labels."""
    raise NotImplementedError("TODO: implement risk metrics")


def evaluate_anomaly(y_true: Any, y_pred: Any) -> dict[str, Any]:
    """TODO: precision on labeled anomaly events when available."""
    raise NotImplementedError("TODO: implement anomaly metrics")
