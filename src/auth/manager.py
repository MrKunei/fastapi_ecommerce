from typing import Optional, Union

from fastapi import Depends, Request
from fastapi_users import BaseUserManager, IntegerIDMixin, models, schemas

from .models import User
from .utils import get_user_db
from src.config import settings


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = settings.SECRET_AUTH
    verification_token_secret = settings.SECRET_AUTH

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")

    async def validate_password(
        self, password: str, user: Union[schemas.UC, models.UP]
    ) -> None:
        ...


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)

