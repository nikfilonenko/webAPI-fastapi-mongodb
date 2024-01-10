import asyncio
import os
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient
from faker import Faker
from datetime import datetime
import random

load_dotenv()

fake = Faker()

async def generate_data():
    mongo_db_name = os.getenv("MONGO_DB_NAME")
    mongo_uri = os.getenv("MONGO_URI")

    client = AsyncIOMotorClient(mongo_uri)
    db = client[mongo_db_name]
    collection = db[mongo_db_name]

    for _ in range(10000):
        document = {
            'title': fake.sentence(),
            'author': fake.name(),
            'published': datetime.combine(fake.date_this_decade(), datetime.min.time()),
            'price': round(random.uniform(10, 100), 2),
            'quantity': random.randint(1, 100),
        }
        await collection.insert_one(document)

    print("Генерация данных завершена.")

asyncio.run(generate_data())
