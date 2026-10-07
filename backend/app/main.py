from fastapi import FastAPI
from app.modules.users.router import router as users_router

app = FastAPI(title="Stock App API", version="1.0.0")

app.include_router(users_router, prefix="/api/v1")

@app.get("/health")
def health():
    return {"status": "ok"}