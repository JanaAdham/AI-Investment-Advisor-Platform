from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class UserInterest(Base):
    __tablename__ = "user_interests"

    interest_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[str] = mapped_column(String(36))
    interest: Mapped[str] = mapped_column(String(100))