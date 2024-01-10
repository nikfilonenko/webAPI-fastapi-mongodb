from decimal import Decimal

from pydantic import BaseModel
from datetime import datetime


class Book(BaseModel):
    title: str
    author: str
    price: Decimal
    published: datetime


class BookInDB(Book):
    id: str


class Publisher(BaseModel):
    name: str