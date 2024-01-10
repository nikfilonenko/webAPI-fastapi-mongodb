from fastapi import APIRouter, Depends
from typing import List
from motor.motor_asyncio import AsyncIOMotorDatabase
from src.database import get_database
from src.models import ProductModel, ProductModelInDB

router = APIRouter()

@router.get("/product_models/", response_model=List[ProductModelInDB])
async def get_all_product_models(db: AsyncIOMotorDatabase = Depends(get_database)):
    product_models = await db.product_models.find().to_list(1000)
    return [ProductModelInDB(**product_model, id=str(product_model["_id"])) for product_model in product_models]
