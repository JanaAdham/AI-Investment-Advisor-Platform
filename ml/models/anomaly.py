"""Anomaly check vs historical behavior (unusual % move).

TODO: z-score of latest return vs rolling mean/std.
TODO: severity thresholds (e.g. |z| >= 2 watch, |z| >= 3 alert).
"""

from __future__ import annotations

from typing import Any


def detect_anomaly(
    ticker: str,
    observed_return: float | None = None,
    history: Any = None,
) -> dict[str, Any]:
    """Flag an unusual percent move versus historical behavior.

    TODO: implement statistical anomaly check.
    """
    raise NotImplementedError("TODO: implement anomaly detection vs history")
