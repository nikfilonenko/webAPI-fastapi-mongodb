from pydantic import BaseModel
from datetime import datetime


class Book(BaseModel):
    title: str
    author: str
    published: datetime


class BookInDB(Book):
    id: str