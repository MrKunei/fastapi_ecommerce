from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_async_session
from .models import Product
from .schemas import ProductCreate, ProductRead
from src.auth.config import current_user
from src.auth.models import User


router = APIRouter(
    prefix="/products",
    tags=["Product"]
)


@router.get('/', response_model=List[ProductRead])
async def get_list_products(user: User = Depends(current_user), session: AsyncSession = Depends(get_async_session)):
    query = select(Product).where(Product.is_active == True)
    result = await session.execute(query)
    return result.scalars().all()


@router.post('/')
async def add_product(new_prod: ProductCreate, user: User = Depends(current_user), session: AsyncSession = Depends(get_async_session)):
    product = insert(Product).values(**new_prod.dict())
    await session.execute(product)
    await session.commit()
    return {'status': 'success'}
