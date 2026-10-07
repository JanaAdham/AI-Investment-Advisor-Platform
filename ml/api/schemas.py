"""Pydantic request/response models mirroring api/contracts JSON Schema.

These shapes are the Spring Boot contract. Phase 0 has no model logic.
"""

from __future__ import annotations

from datetime import date, datetime
from typing import Literal

from pydantic import BaseModel, Field

DISCLAIMER = (
    "Decision support only. Not financial advice. No guaranteed returns. "
    "This service does not execute trades."
)
PLACEHOLDER_EXPLANATION = "Phase 0 placeholder. Model is not implemented."
MODEL_VERSION = "0.0.0-phase0"


class SentimentRequest(BaseModel):
    text: str = Field(..., min_length=1)
    ticker: str | None = None
    published_at: datetime | None = None


class SentimentProbabilities(BaseModel):
    positive: float = Field(..., ge=0, le=1)
    neutral: float = Field(..., ge=0, le=1)
    negative: float = Field(..., ge=0, le=1)


class SentimentResponse(BaseModel):
    label: Literal["positive", "neutral", "negative"]
    probabilities: SentimentProbabilities
    confidence: float = Field(..., ge=0, le=1)
    explanation: str
    disclaimer: str
    model_version: str


class RiskRequest(BaseModel):
    ticker: str = Field(..., min_length=1)
    as_of: date | None = None
    lookback_days: int | None = Field(default=None, ge=1)


class ContributingFactor(BaseModel):
    name: str
    value: float
    contribution: float
    direction: str


class RiskResponse(BaseModel):
    ticker: str
    risk_score: float = Field(..., ge=0, le=100)
    risk_level: Literal["low", "medium", "high"]
    contributing_factors: list[ContributingFactor]
    confidence: float = Field(..., ge=0, le=1)
    explanation: str
    disclaimer: str
    model_version: str


class ForecastRequest(BaseModel):
    ticker: str = Field(..., min_length=1)
    horizon_days: Literal[1, 5]
    as_of: date | None = None


class ForecastInterval(BaseModel):
    lower: float
    upper: float
    confidence_level: float = Field(..., ge=0, le=1)


class ForecastResponse(BaseModel):
    ticker: str
    target: Literal["return"] = "return"
    horizon_days: Literal[1, 5]
    point_forecast: float
    interval: ForecastInterval
    method: str
    explanation: str
    disclaimer: str
    model_version: str


class AnomalyRequest(BaseModel):
    ticker: str = Field(..., min_length=1)
    as_of: date | None = None
    observed_return: float | None = None
    lookback_days: int | None = Field(default=None, ge=1)


class AnomalyResponse(BaseModel):
    ticker: str
    is_anomaly: bool
    severity: Literal["none", "watch", "alert"]
    observed_return: float
    z_score: float
    threshold: float
    explanation: str
    disclaimer: str
    model_version: str


class HealthResponse(BaseModel):
    status: Literal["ok"]
