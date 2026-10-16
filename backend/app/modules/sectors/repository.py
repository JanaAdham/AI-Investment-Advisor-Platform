from sqlalchemy import select
from sqlalchemy.orm import Session

from .models import Sector


def get_by_id(db: Session, sector_id: int) -> Sector | None:
    return db.get(Sector, sector_id)


def get_by_name(db: Session, name: str) -> Sector | None:
    return db.scalar(select(Sector).where(Sector.sector_name == name))


def list_sectors(db: Session, skip: int = 0, limit: int = 20) -> list[Sector]:
    stmt = select(Sector).order_by(Sector.sector_id).offset(skip).limit(limit)
    return list(db.scalars(stmt))


def create(db: Session, sector: Sector) -> Sector:
    db.add(sector)
    db.commit()
    db.refresh(sector)
    return sector


def update(db: Session, sector: Sector, name: str) -> Sector:
    sector.sector_name = name
    db.commit()
    db.refresh(sector)
    return sector


def delete(db: Session, sector: Sector) -> None:
    db.delete(sector)
    db.commit()