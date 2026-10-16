from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.core.security import hash_password
from . import repository
from .models import User
from .schemas import UserCreate, UserUpdate


def create_user(db: Session, data: UserCreate) -> User:
    email = data.email.lower()
    if repository.get_by_email(db, email):
        raise HTTPException(status.HTTP_409_CONFLICT, "Email already registered")
    user = User(
        first_name=data.first_name,
        last_name=data.last_name,
        email=email,
        password_hash=hash_password(data.password),
        age=data.age,
        country=data.country,
        timezone=data.timezone,
    )
    return repository.create(db, user)


def get_user(db: Session, user_id: str) -> User:
    user = repository.get_by_id(db, user_id)
    if not user:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "User not found")
    return user


def list_users(db: Session, skip: int, limit: int) -> list[User]:
    return repository.list_users(db, skip, limit)


def update_user(db: Session, user_id: str, data: UserUpdate) -> User:
    user = get_user(db, user_id)
    changes = data.model_dump(exclude_unset=True)
    return repository.update(db, user, changes)


def delete_user(db: Session, user_id: str) -> None:
    user = get_user(db, user_id)
    repository.delete(db, user)