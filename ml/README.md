# AI Investment Advisor — ML service (Phase 0)

Decision-support ML API for the Spring Boot backend. Endpoints return **structured JSON**, not HTML. This service analyzes companies, portfolios, markets, and news. It does **not** execute trades and never claims guaranteed returns.

Phase 0 is **structure and contracts only**: folder layout, JSON Schema / Pydantic shapes, and FastAPI stubs that return placeholder JSON. There is no sample data, feature math, or trained models yet.

## Layout

```
ml/
  api/           FastAPI app, Pydantic models, JSON Schema contracts
  data/          MarketDataSource protocol (unimplemented)
  features/      OHLCV feature stubs
  models/        sentiment, risk, forecast, anomaly stubs
  evaluation/    metrics stubs
  notebooks/     empty (no analysis notebooks in Phase 0)
```

## Run locally

Python 3.11+. From the `ml/` directory:

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
# source .venv/bin/activate

pip install -r requirements.txt
uvicorn api.main:app --reload
```

- Health: `GET http://127.0.0.1:8000/health`
- OpenAPI: `http://127.0.0.1:8000/docs`
- Example: `POST /v1/sentiment` with `{"text": "Company reports record revenue"}`

Placeholder responses include `explanation`, `disclaimer`, and `model_version`. They are not model output.

JSON Schema files for Spring Boot live in `api/contracts/`.

## Deferred (not in Phase 0)

- Local public sample datasets (CSV) and Azure Bronze→Silver / Databricks adapters
- Real OHLCV feature engineering
- Model implementations (baselines, FinBERT wrap, training loop)
- Evaluation metrics wiring and analysis notebooks
- UI
- Trade execution (never)
- Any claim of guaranteed returns (never)
