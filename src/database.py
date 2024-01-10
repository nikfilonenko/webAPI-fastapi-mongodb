from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from dotenv import load_dotenv
import os

load_dotenv()


class MongoDB:
    client: AsyncIOMotorClient = None


async def connect_to_mongo():
    if MongoDB.client is None:
        mongo_db_name = os.getenv("MONGO_DB_NAME")
        mongo_uri = os.getenv("MONGO_URI")
        MongoDB.client = AsyncIOMotorClient(mongo_uri)


async def close_mongo_connection():
    if MongoDB.client is not None:
        MongoDB.client.close()


async def get_database() -> AsyncIOMotorDatabase:
    return MongoDB.client[os.getenv("MONGO_DB_NAME")]
