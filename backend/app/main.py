from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.modules.auth.router import router as auth_router
from app.modules.sectors.router import router as sectors_router
from app.modules.user_interests.router import router as interests_router
from app.modules.user_preference.router import router as preferences_router
from app.modules.users.router import router as users_router

app = FastAPI(title="Stock App API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix="/api/v1")
app.include_router(users_router, prefix="/api/v1")
app.include_router(sectors_router, prefix="/api/v1")
app.include_router(interests_router, prefix="/api/v1")
app.include_router(preferences_router, prefix="/api/v1")


@app.get("/health")
def health():
    return {"status": "ok"}