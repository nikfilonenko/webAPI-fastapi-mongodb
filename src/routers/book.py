from bson import ObjectId
from fastapi import APIRouter, Depends, HTTPException
from typing import List
from motor.motor_asyncio import AsyncIOMotorDatabase
from src.database import get_database
from src.models import Book, BookInDB

router = APIRouter()

@router.get("/books/", response_model=List[BookInDB])
async def get_all_books(db: AsyncIOMotorDatabase = Depends(get_database)):
    books = await db.books.find().to_list(1000)
    return [BookInDB(**book, id=str(book["_id"])) for book in books]


@router.get("/books/{book_id}", response_model=BookInDB)
async def read_book(book_id: str, db: AsyncIOMotorDatabase = Depends(get_database)):
    book = await db.books.find_one({"_id": ObjectId(book_id)})
    if book:
        return BookInDB(**book, id=str(book["_id"]))
    raise HTTPException(status_code=404, detail="Book not found")


@router.post("/books/", response_model=List[BookInDB])
async def delete_all_books(db: AsyncIOMotorDatabase = Depends(get_database)):
    await db.books.delete_many()
    return []
