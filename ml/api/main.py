"""FastAPI skeleton for Spring Boot. Phase 0 returns placeholder JSON only."""

from __future__ import annotations

from fastapi import FastAPI

from api.schemas import (
    DISCLAIMER,
    MODEL_VERSION,
    PLACEHOLDER_EXPLANATION,
    AnomalyRequest,
    AnomalyResponse,
    ForecastInterval,
    ForecastRequest,
    ForecastResponse,
    HealthResponse,
    RiskRequest,
    RiskResponse,
    SentimentProbabilities,
    SentimentRequest,
    SentimentResponse,
)

app = FastAPI(
    title="AI Investment Advisor ML",
    description=(
        "Decision-support ML API. Returns structured JSON for Spring Boot. "
        "Phase 0 endpoints are placeholders with no model logic."
    ),
    version=MODEL_VERSION,
)


@app.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse(status="ok")


@app.post("/v1/sentiment", response_model=SentimentResponse)
def sentiment(request: SentimentRequest) -> SentimentResponse:
    # TODO: call models.sentiment.classify_sentiment (no logic in Phase 0).
    _ = request
    return SentimentResponse(
        label="neutral",
        probabilities=SentimentProbabilities(
            positive=0.0, neutral=1.0, negative=0.0
        ),
        confidence=0.0,
        explanation=PLACEHOLDER_EXPLANATION,
        disclaimer=DISCLAIMER,
        model_version=MODEL_VERSION,
    )


@app.post("/v1/risk", response_model=RiskResponse)
def risk(request: RiskRequest) -> RiskResponse:
    # TODO: load features and call models.risk.score_risk (no logic in Phase 0).
    return RiskResponse(
        ticker=request.ticker,
        risk_score=0.0,
        risk_level="low",
        contributing_factors=[],
        confidence=0.0,
        explanation=PLACEHOLDER_EXPLANATION,
        disclaimer=DISCLAIMER,
        model_version=MODEL_VERSION,
    )


@app.post("/v1/forecast", response_model=ForecastResponse)
def forecast(request: ForecastRequest) -> ForecastResponse:
    # TODO: call models.forecast.forecast_return (no logic in Phase 0).
    return ForecastResponse(
        ticker=request.ticker,
        target="return",
        horizon_days=request.horizon_days,
        point_forecast=0.0,
        interval=ForecastInterval(lower=0.0, upper=0.0, confidence_level=0.0),
        method="placeholder",
        explanation=PLACEHOLDER_EXPLANATION,
        disclaimer=DISCLAIMER,
        model_version=MODEL_VERSION,
    )


@app.post("/v1/anomaly", response_model=AnomalyResponse)
def anomaly(request: AnomalyRequest) -> AnomalyResponse:
    # TODO: call models.anomaly.detect_anomaly (no logic in Phase 0).
    return AnomalyResponse(
        ticker=request.ticker,
        is_anomaly=False,
        severity="none",
        observed_return=request.observed_return if request.observed_return is not None else 0.0,
        z_score=0.0,
        threshold=0.0,
        explanation=PLACEHOLDER_EXPLANATION,
        disclaimer=DISCLAIMER,
        model_version=MODEL_VERSION,
    )
