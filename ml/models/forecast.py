"""Simple return forecast with uncertainty.

TODO: historical-mean baseline + interval from historical volatility.
TODO: train a simple lagged linear model (features, training loop, metrics).
"""

from __future__ import annotations

from typing import Any


def forecast_return(
    ticker: str, horizon_days: int, features: dict[str, Any] | None = None
) -> dict[str, Any]:
    """Point forecast of return plus an uncertainty interval.

    TODO: implement forecast; never claim guaranteed returns.
    """
    raise NotImplementedError("TODO: implement return forecast with uncertainty")
