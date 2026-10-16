from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.core.security import verify_password
from app.modules.users import repository
from app.modules.users.models import User


def authenticate(db: Session, email: str, password: str) -> User:
    user = repository.get_by_email(db, email.lower())
    # same error for "no such email" and "wrong password" on purpose,
    # so nobody can use login to find out which emails are registered
    if not user or not verify_password(password, user.password_hash):
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Invalid email or password")
    if user.status != "ACTIVE":
        raise HTTPException(status.HTTP_403_FORBIDDEN, "Account is not active")
    return user