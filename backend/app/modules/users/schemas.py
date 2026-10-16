from pydantic import BaseModel, EmailStr, Field, ConfigDict


class UserCreate(BaseModel):
    first_name: str = Field(min_length=1, max_length=50)
    last_name: str = Field(min_length=1, max_length=50)
    email: EmailStr
    password: str = Field(min_length=8, max_length=72)
    age: int = Field(ge=13, le=120)
    country: str = Field(min_length=1, max_length=100)
    timezone: str = Field(default="Africa/Cairo", max_length=64)


class UserUpdate(BaseModel):
    first_name: str | None = Field(default=None, min_length=1, max_length=50)
    last_name: str | None = Field(default=None, min_length=1, max_length=50)
    age: int | None = Field(default=None, ge=13, le=120)
    country: str | None = Field(default=None, min_length=1, max_length=100)
    timezone: str | None = Field(default=None, max_length=64)
    profile_image_url: str | None = Field(default=None, max_length=500)


class UserOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    user_id: str
    first_name: str
    last_name: str
    email: EmailStr
    age: int
    country: str
    timezone: str
    profile_image_url: str | None = None
    email_verified: bool