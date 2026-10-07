"""Company risk score from financial + market features.

TODO: transparent weighted score (not a black-box sklearn pipeline).
TODO: contributing factors for explanations.
"""

from __future__ import annotations

from typing import Any


def score_risk(ticker: str, features: dict[str, Any] | None = None) -> dict[str, Any]:
    """Return a 0–100 risk score with contributing factors.

    TODO: implement a documented, explainable scoring formula.
    """
    raise NotImplementedError("TODO: implement explainable company risk score")
