from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from . import service
from .schemas import UserOut

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/{user_id}", response_model=UserOut)
def read_user(user_id: str, db: Session = Depends(get_db)):
    return service.get_user(db, user_id)