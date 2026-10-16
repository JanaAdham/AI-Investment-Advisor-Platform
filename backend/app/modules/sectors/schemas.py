from pydantic import BaseModel, ConfigDict, Field


class SectorCreate(BaseModel):
    sector_name: str = Field(min_length=1, max_length=100)


class SectorUpdate(BaseModel):
    sector_name: str = Field(min_length=1, max_length=100)


class SectorOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    sector_id: int
    sector_name: str