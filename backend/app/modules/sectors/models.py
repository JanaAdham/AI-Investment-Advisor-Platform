from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Sector(Base):
    __tablename__ = "sectors"

    sector_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    sector_name: Mapped[str] = mapped_column(String(100), unique=True)