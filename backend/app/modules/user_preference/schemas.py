from pydantic import BaseModel, ConfigDict, Field


class UserPreferenceCreate(BaseModel):
    user_id: str = Field(min_length=1, max_length=36)
    investment_goal: str | None = Field(default=None, max_length=100)


class UserPreferenceUpdate(BaseModel):
    investment_goal: str | None = Field(default=None, max_length=100)


class UserPreferenceOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    preference_id: int
    user_id: str
    investment_goal: str | None = None