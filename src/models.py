from decimal import Decimal
from pydantic import BaseModel
from datetime import datetime


class ProductModel(BaseModel):
    name: str
    description: str


class Publisher(BaseModel):
    name: str


class Book(BaseModel):
    title: str
    author: str
    price: Decimal
    published: datetime
    publisher: Publisher
    product_model: ProductModel


class BookInDB(Book):
    id: str

class PublisherInDB(Publisher):
    id: str

class ProductModelInDB(ProductModel):
    id: str
