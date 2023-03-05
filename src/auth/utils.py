from typing import Optional

from fastapi import Depends
from fastapi_users.db import SQLAlchemyUserDatabase
from fastapi_users.models import UP
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from .models import User

import sys
sys.path.append("..")

from src.database import get_async_session


class MySQLAlchemyDatabase(SQLAlchemyUserDatabase):
    async def get_by_email(self, phone_email: str) -> Optional[UP]:
        statement = select(self.user_table).where(
            (func.lower(self.user_table.email) == func.lower(phone_email)) |
            (func.lower(self.user_table.phone) == func.lower(phone_email))
        )
        result = await self._get_user(statement)

        return result


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield MySQLAlchemyDatabase(session, User)
