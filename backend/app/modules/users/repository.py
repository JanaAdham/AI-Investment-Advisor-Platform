from sqlalchemy.orm import Session
from sqlalchemy import select
from .models import User

def get_by_id(db: Session, user_id: str) -> User | None:
    return db.get(User, user_id)

def get_by_email(db: Session, email: str) -> User | None:
    return db.scalar(select(User).where(User.email == email))

def list_users(db: Session, skip: int = 0, limit: int = 20) -> list[User]:
    return list(db.scalars(select(User).offset(skip).limit(limit)))

def create(db: Session, user: User) -> User:
    db.add(user)
    db.commit()
    db.refresh(user)
    return user