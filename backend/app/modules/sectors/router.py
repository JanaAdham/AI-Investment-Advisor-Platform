from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from . import service
from .schemas import SectorCreate, SectorOut, SectorUpdate

router = APIRouter(prefix="/sectors", tags=["sectors"])


@router.post("", response_model=SectorOut, status_code=status.HTTP_201_CREATED)
def create_sector(data: SectorCreate, db: Session = Depends(get_db)):
    return service.create_sector(db, data)


@router.get("", response_model=list[SectorOut])
def list_sectors(
    skip: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=100),
    db: Session = Depends(get_db),
):
    return service.list_sectors(db, skip, limit)


@router.get("/{sector_id}", response_model=SectorOut)
def read_sector(sector_id: int, db: Session = Depends(get_db)):
    return service.get_sector(db, sector_id)


@router.put("/{sector_id}", response_model=SectorOut)
def update_sector(sector_id: int, data: SectorUpdate, db: Session = Depends(get_db)):
    return service.update_sector(db, sector_id, data)


@router.delete("/{sector_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_sector(sector_id: int, db: Session = Depends(get_db)):
    service.delete_sector(db, sector_id)