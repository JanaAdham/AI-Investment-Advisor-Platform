from sqlalchemy import select
from sqlalchemy.orm import Session

from .models import UserInterest


def get_by_id(db: Session, interest_id: int) -> UserInterest | None:
    return db.get(UserInterest, interest_id)


def get_by_user_and_name(db: Session, user_id: str, interest: str) -> UserInterest | None:
    stmt = select(UserInterest).where(
        UserInterest.user_id == user_id, UserInterest.interest == interest
    )
    return db.scalar(stmt)


def list_interests(
    db: Session, user_id: str | None = None, skip: int = 0, limit: int = 20
) -> list[UserInterest]:
    stmt = select(UserInterest)
    if user_id:
        stmt = stmt.where(UserInterest.user_id == user_id)
    stmt = stmt.order_by(UserInterest.interest_id).offset(skip).limit(limit)
    return list(db.scalars(stmt))


def create(db: Session, item: UserInterest) -> UserInterest:
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def update(db: Session, item: UserInterest, interest: str) -> UserInterest:
    item.interest = interest
    db.commit()
    db.refresh(item)
    return item


def delete(db: Session, item: UserInterest) -> None:
    db.delete(item)
    db.commit()