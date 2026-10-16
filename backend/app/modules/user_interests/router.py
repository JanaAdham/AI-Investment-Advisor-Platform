from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from . import service
from .schemas import UserInterestCreate, UserInterestOut, UserInterestUpdate

router = APIRouter(prefix="/user-interests", tags=["user-interests"])


@router.post("", response_model=UserInterestOut, status_code=status.HTTP_201_CREATED)
def create_interest(data: UserInterestCreate, db: Session = Depends(get_db)):
    return service.create_interest(db, data)


@router.get("", response_model=list[UserInterestOut])
def list_interests(
    user_id: str | None = None,
    skip: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=100),
    db: Session = Depends(get_db),
):
    return service.list_interests(db, user_id, skip, limit)


@router.get("/{interest_id}", response_model=UserInterestOut)
def read_interest(interest_id: int, db: Session = Depends(get_db)):
    return service.get_interest(db, interest_id)


@router.put("/{interest_id}", response_model=UserInterestOut)
def update_interest(
    interest_id: int, data: UserInterestUpdate, db: Session = Depends(get_db)
):
    return service.update_interest(db, interest_id, data)


@router.delete("/{interest_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_interest(interest_id: int, db: Session = Depends(get_db)):
    service.delete_interest(db, interest_id)