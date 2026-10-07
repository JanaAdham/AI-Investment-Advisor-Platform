from pydantic import BaseModel, EmailStr, Field, ConfigDict

class UserCreate(BaseModel):
    first_name: str = Field(min_length=1, max_length=50)
    last_name: str = Field(min_length=1, max_length=50)
    email: EmailStr
    password: str = Field(min_length=8)
    age: int = Field(ge=13, le=120)
    country: str
    timezone: str

class UserOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    first_name: str
    last_name: str
    email: EmailStr
    email_verified: bool