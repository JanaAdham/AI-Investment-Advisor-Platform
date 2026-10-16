from pydantic import BaseModel, ConfigDict, Field


class UserInterestCreate(BaseModel):
    user_id: str = Field(min_length=1, max_length=36)
    interest: str = Field(min_length=1, max_length=100)


class UserInterestUpdate(BaseModel):
    interest: str = Field(min_length=1, max_length=100)


class UserInterestOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    interest_id: int
    user_id: str
    interest: str