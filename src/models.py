from pydantic import BaseModel
from datetime import datetime


class ProductModel(BaseModel):
    description: str


class Publisher(BaseModel):
    name: str


class Book(BaseModel):
    title: str
    author: str
    price: float
    published: datetime
    publisher: Publisher
    product_model: ProductModel


class BookInDB(Book):
    id: str

class PublisherInDB(Publisher):
    id: str

class ProductModelInDB(ProductModel):
    id: str
