from sqlalchemy import select
from sqlalchemy.orm import Session

from .models import User


def get_by_id(db: Session, user_id: str) -> User | None:
    return db.get(User, user_id)


def get_by_email(db: Session, email: str) -> User | None:
    return db.scalar(select(User).where(User.email == email))


def list_users(db: Session, skip: int = 0, limit: int = 30) -> list[User]:
    return list(db.scalars(select(User).offset(skip).limit(limit)))


def create(db: Session, user: User) -> User:
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def update(db: Session, user: User, changes: dict) -> User:
    for field, value in changes.items():
        setattr(user, field, value)
    db.commit()
    db.refresh(user)
    return user


def delete(db: Session, user: User) -> None:
    db.delete(user)
    db.commit()