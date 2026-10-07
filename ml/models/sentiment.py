"""Financial news sentiment classification (positive / neutral / negative).

TODO: lexicon/keyword baseline behind the API schema.
TODO: wrap an evaluated pretrained model (e.g. FinBERT) behind the same schema.
"""

from __future__ import annotations

from typing import Any


def classify_sentiment(text: str, ticker: str | None = None) -> dict[str, Any]:
    """Classify news text into positive, neutral, or negative.

    TODO: implement classification and return probabilities + explanation.
    """
    raise NotImplementedError("TODO: implement sentiment classification")
