from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.modules.users import repository as users_repository
from . import repository
from .models import UserInterest
from .schemas import UserInterestCreate, UserInterestUpdate


def _clean(text: str) -> str:
    text = text.strip()
    if not text:
        raise HTTPException(
            status.HTTP_422_UNPROCESSABLE_ENTITY, "Interest cannot be empty"
        )
    return text


def create_interest(db: Session, data: UserInterestCreate) -> UserInterest:
    if not users_repository.get_by_id(db, data.user_id):
        raise HTTPException(status.HTTP_404_NOT_FOUND, "User not found")
    interest = _clean(data.interest)
    if repository.get_by_user_and_name(db, data.user_id, interest):
        raise HTTPException(status.HTTP_409_CONFLICT, "Interest already exists for this user")
    return repository.create(db, UserInterest(user_id=data.user_id, interest=interest))


def get_interest(db: Session, interest_id: int) -> UserInterest:
    item = repository.get_by_id(db, interest_id)
    if not item:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Interest not found")
    return item


def list_interests(
    db: Session, user_id: str | None, skip: int, limit: int
) -> list[UserInterest]:
    return repository.list_interests(db, user_id, skip, limit)


def update_interest(db: Session, interest_id: int, data: UserInterestUpdate) -> UserInterest:
    item = get_interest(db, interest_id)
    interest = _clean(data.interest)
    existing = repository.get_by_user_and_name(db, item.user_id, interest)
    if existing and existing.interest_id != item.interest_id:
        raise HTTPException(status.HTTP_409_CONFLICT, "Interest already exists for this user")
    return repository.update(db, item, interest)


def delete_interest(db: Session, interest_id: int) -> None:
    item = get_interest(db, interest_id)
    repository.delete(db, item)