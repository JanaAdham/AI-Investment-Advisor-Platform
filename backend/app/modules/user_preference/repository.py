from sqlalchemy import select
from sqlalchemy.orm import Session

from .models import UserPreference


def get_by_id(db: Session, preference_id: int) -> UserPreference | None:
    return db.get(UserPreference, preference_id)


def get_by_user(db: Session, user_id: str) -> UserPreference | None:
    return db.scalar(select(UserPreference).where(UserPreference.user_id == user_id))


def list_preferences(
    db: Session, user_id: str | None = None, skip: int = 0, limit: int = 20
) -> list[UserPreference]:
    stmt = select(UserPreference)
    if user_id:
        stmt = stmt.where(UserPreference.user_id == user_id)
    stmt = stmt.order_by(UserPreference.preference_id).offset(skip).limit(limit)
    return list(db.scalars(stmt))


def create(db: Session, pref: UserPreference) -> UserPreference:
    db.add(pref)
    db.commit()
    db.refresh(pref)
    return pref


def update(db: Session, pref: UserPreference, changes: dict) -> UserPreference:
    for field, value in changes.items():
        setattr(pref, field, value)
    db.commit()
    db.refresh(pref)
    return pref


def delete(db: Session, pref: UserPreference) -> None:
    db.delete(pref)
    db.commit()