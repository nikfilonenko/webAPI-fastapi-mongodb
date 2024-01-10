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

        db = MongoDB.client[mongo_db_name]

        collection = db[mongo_db_name]

        result = await collection.create_index([("title", "text"), ("author", "text"), ("description", "text")])
        print(result)

async def close_mongo_connection():
    if MongoDB.client is not None:
        MongoDB.client.close()

async def get_database() -> AsyncIOMotorDatabase:
    return MongoDB.client[os.getenv("MONGO_DB_NAME")]
