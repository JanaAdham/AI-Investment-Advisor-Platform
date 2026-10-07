"""OHLCV feature engineering.

TODO: log returns
TODO: rolling mean/std (20d)
TODO: realized volatility (20d, 60d)
TODO: max drawdown over the window
TODO: volume z-score
TODO: simple momentum (close vs SMA20)
"""

from __future__ import annotations

from typing import Any


def compute_ohlcv_features(ohlcv: Any) -> dict[str, Any]:
    """Build named market features from an OHLCV window.

    TODO: implement with pandas/numpy (no sklearn pipeline).
    """
    raise NotImplementedError(
        "TODO: compute OHLCV features (returns, vol, drawdown, volume z-score)"
    )
