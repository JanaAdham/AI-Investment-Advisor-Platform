from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from . import service
from .schemas import UserCreate, UserOut, UserUpdate

router = APIRouter(prefix="/users", tags=["users"])


@router.post("", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def create_user(data: UserCreate, db: Session = Depends(get_db)):
    return service.create_user(db, data)


@router.get("", response_model=list[UserOut])
def list_users(
    skip: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=100),
    db: Session = Depends(get_db),
):
    return service.list_users(db, skip, limit)


@router.get("/{user_id}", response_model=UserOut)
def read_user(user_id: str, db: Session = Depends(get_db)):
    return service.get_user(db, user_id)


@router.put("/{user_id}", response_model=UserOut)
def update_user(user_id: str, data: UserUpdate, db: Session = Depends(get_db)):
    return service.update_user(db, user_id, data)


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: str, db: Session = Depends(get_db)):
    service.delete_user(db, user_id)