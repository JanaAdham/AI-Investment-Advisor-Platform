from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from . import repository
from .models import User
from .schemas import UserCreate

def create_user(db: Session, data: UserCreate, password_hash: str) -> User:
    email = data.email.lower()
    if repository.get_by_email(db, email):
        raise HTTPException(status.HTTP_409_CONFLICT, "Email already registered")
    user = User(
        first_name=data.first_name,
        last_name=data.last_name,
        email=email,
        password_hash=password_hash,
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