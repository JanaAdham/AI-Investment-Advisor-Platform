from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from . import repository
from .models import Sector
from .schemas import SectorCreate, SectorUpdate


def _clean_name(name: str) -> str:
    name = name.strip()
    if not name:
        raise HTTPException(
            status.HTTP_422_UNPROCESSABLE_ENTITY, "Sector name cannot be empty"
        )
    return name


def create_sector(db: Session, data: SectorCreate) -> Sector:
    name = _clean_name(data.sector_name)
    if repository.get_by_name(db, name):
        raise HTTPException(status.HTTP_409_CONFLICT, "Sector already exists")
    return repository.create(db, Sector(sector_name=name))


def get_sector(db: Session, sector_id: int) -> Sector:
    sector = repository.get_by_id(db, sector_id)
    if not sector:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Sector not found")
    return sector


def list_sectors(db: Session, skip: int, limit: int) -> list[Sector]:
    return repository.list_sectors(db, skip, limit)


def update_sector(db: Session, sector_id: int, data: SectorUpdate) -> Sector:
    sector = get_sector(db, sector_id)
    name = _clean_name(data.sector_name)
    existing = repository.get_by_name(db, name)
    if existing and existing.sector_id != sector.sector_id:
        raise HTTPException(status.HTTP_409_CONFLICT, "Sector already exists")
    return repository.update(db, sector, name)


def delete_sector(db: Session, sector_id: int) -> None:
    sector = get_sector(db, sector_id)
    repository.delete(db, sector)