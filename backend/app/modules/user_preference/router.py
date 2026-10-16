from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from . import service
from .schemas import UserPreferenceCreate, UserPreferenceOut, UserPreferenceUpdate

router = APIRouter(prefix="/user-preferences", tags=["user-preferences"])


@router.post("", response_model=UserPreferenceOut, status_code=status.HTTP_201_CREATED)
def create_preference(data: UserPreferenceCreate, db: Session = Depends(get_db)):
    return service.create_preference(db, data)


@router.get("", response_model=list[UserPreferenceOut])
def list_preferences(
    user_id: str | None = None,
    skip: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=100),
    db: Session = Depends(get_db),
):
    return service.list_preferences(db, user_id, skip, limit)


@router.get("/{preference_id}", response_model=UserPreferenceOut)
def read_preference(preference_id: int, db: Session = Depends(get_db)):
    return service.get_preference(db, preference_id)


@router.put("/{preference_id}", response_model=UserPreferenceOut)
def update_preference(
    preference_id: int, data: UserPreferenceUpdate, db: Session = Depends(get_db)
):
    return service.update_preference(db, preference_id, data)


@router.delete("/{preference_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_preference(preference_id: int, db: Session = Depends(get_db)):
    service.delete_preference(db, preference_id)