import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from faker import Faker
from datetime import datetime
import random

fake = Faker()

async def generate_data():
    client = AsyncIOMotorClient('mongodb://localhost:27017/')
    db = client['books']
    collection = db['books']

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
