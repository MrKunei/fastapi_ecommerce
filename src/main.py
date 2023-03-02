from fastapi import FastAPI
from fastapi_users import fastapi_users

from .auth.config import auth_backend
from .auth.schemas import UserRead, UserCreate

app = FastAPI(title='Ecommerce API')


app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)