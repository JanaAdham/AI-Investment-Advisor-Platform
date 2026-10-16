from pydantic import BaseModel, EmailStr

from app.modules.users.schemas import UserOut


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class LoginResponse(BaseModel):
    message: str
    user: UserOut