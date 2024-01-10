from fastapi import APIRouter, Depends
from typing import List
from motor.motor_asyncio import AsyncIOMotorDatabase
from src.database import get_database
from src.models import Publisher, PublisherInDB

router = APIRouter()

@router.get("/publishers/", response_model=List[PublisherInDB])
async def get_all_publishers(db: AsyncIOMotorDatabase = Depends(get_database)):
    publishers = await db.publishers.find().to_list(1000)

    return [PublisherInDB(**publisher, id=str(publisher["_id"])) for publisher in publishers]

