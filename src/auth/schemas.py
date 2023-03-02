from typing import Optional
from fastapi_users import schemas
from pydantic import EmailStr, Field


class UserRead(schemas.BaseUser[int]):
    id: int
    username: str
    email: str
    phone: str
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False

    class Config:
        orm_mode = True


class UserCreate(schemas.BaseUserCreate):
    username: str
    email: EmailStr
    phone: str = Field(regex="^[\+][7][0-9]{10}$")
    password: str = Field(regex="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$%&!:])[A-Za-z\d@$%&!:]{8,}$")
    repeat_password: str = Field(regex="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$%&!:])[A-Za-z\d@$%&!:]{8,}$")

    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False
