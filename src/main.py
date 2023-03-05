from fastapi import FastAPI

from auth.config import auth_backend, fastapi_users
from auth.schemas import UserRead, UserCreate
from product.router import router as router_product


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

app.include_router(router_product)
