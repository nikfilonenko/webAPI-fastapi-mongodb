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
        product_model_data = {
            'name': fake.word(),
            'description': fake.sentence(),
        }
        publisher_data = {
            'name': fake.company(),
        }
        book_data = {
            'title': fake.sentence(),
            'author': fake.name(),
            'price': round(random.uniform(10, 100), 2),
            'published': datetime.combine(fake.date_this_decade(), datetime.min.time()),
            'publisher': publisher_data,
            'product_model': product_model_data,
        }

        product_model_result = await db.product_models.insert_one(product_model_data)
        publisher_result = await db.publishers.insert_one(publisher_data)
        book_data['publisher']['id'] = str(publisher_result.inserted_id)
        book_data['product_model']['id'] = str(product_model_result.inserted_id)
        book_result = await collection.insert_one(book_data)

    print("Генерация данных завершена.")


if __name__ == "__main__":
    asyncio.run(generate_data())
