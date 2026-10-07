"""Abstract market-data access for ML pipelines.

TODO: Add a local CSV / public-sample adapter (later phase).
TODO: Add an Azure Silver / Databricks adapter (out of scope for Phase 0).
"""

from __future__ import annotations

from datetime import date
from typing import Any, Protocol


class NewsItem:
    """Placeholder news record.

    TODO: define fields when a sample dataset exists.
    """

    ticker: str | None
    published_at: str | None
    text: str


class MarketDataSource(Protocol):
    """Contract for OHLCV, news, and company info. No implementation in Phase 0."""

    def get_ohlcv(self, ticker: str, start: date, end: date) -> Any:
        """Return OHLCV rows: date, ticker, open, high, low, close, volume.

        TODO: implement via local sample then Azure Silver.
        """
        ...

    def get_news(
        self, ticker: str | None, start: date, end: date
    ) -> list[NewsItem]:
        """Return news items for an optional ticker and date range.

        TODO: implement via local sample then Azure Silver.
        """
        ...

    def get_company_info(self, ticker: str) -> dict[str, Any]:
        """Return company fundamentals / metadata.

        TODO: implement when Silver company-info tables exist.
        """
        ...
