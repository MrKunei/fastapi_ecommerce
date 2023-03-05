from datetime import datetime
from pydantic import BaseModel


class ProductRead(BaseModel):
    id: int
    name: str
    price: float
    created_at: datetime
    updated_at: datetime
    is_active: bool

    class Config:
        orm_mode = True


class ProductCreate(BaseModel):
    name: str
    price: float
    is_active: bool
