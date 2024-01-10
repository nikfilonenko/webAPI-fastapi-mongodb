from bson import ObjectId
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
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


@router.post("/books/", response_model=BookInDB)
async def create_book(book: Book, db: AsyncIOMotorDatabase = Depends(get_database)):
    book_data = book.model_dump()

    if not book_data:
        raise HTTPException(status_code=400, detail="Invalid book data")

    result = await db.books.insert_one(book_data)

    if result.acknowledged:
        created_book = await db.books.find_one({"_id": result.inserted_id})

        if created_book:
            return BookInDB(**created_book, id=str(created_book["_id"]))

    raise HTTPException(status_code=500, detail="Failed to create book")


@router.put("/books/{book_id}", response_model=BookInDB)
async def update_book(book_id: str, updated_book: Book, db: AsyncIOMotorDatabase = Depends(get_database)):
    updated_book_data = updated_book.model_dump(exclude_unset=True)
    result = await db.books.update_one({"_id": ObjectId(book_id)}, {"$set": updated_book_data})

    if result.modified_count == 1:
        updated_book = await db.books.find_one({"_id": ObjectId(book_id)})
        return BookInDB(**updated_book, id=str(updated_book["_id"]))
    else:
        raise HTTPException(status_code=404, detail="Book not found")


@router.delete("/books/{book_id}", response_model=List[BookInDB])
async def delete_book(book_id: str, db: AsyncIOMotorDatabase = Depends(get_database)):
    result = await db.books.delete_one({"_id": ObjectId(book_id)})

    if result.deleted_count == 1:
        books = await db.books.find().to_list(1000)
        return [BookInDB(**book, id=str(book["_id"])) for book in books]
    else:
        raise HTTPException(status_code=404, detail="Book not found")



@router.delete("/books/", response_model=None)
async def delete_all_books(title: str, db: AsyncIOMotorDatabase = Depends(get_database)):
    await db.books.delete_many(filter=title)

    return JSONResponse(content={f"message": f"All books with title {title} deleted successfully"}, status_code=200)



# Поиск по текстовым индексам
@router.get("/books/search/{query}", response_model=List[BookInDB])
async def search_books(query: str, db: AsyncIOMotorDatabase = Depends(get_database)):
    result = await db.books.find(
        {"$text": {"$search": query}},
        {"score": {"$meta": "textScore"}}
    ).sort([("score", {"$meta": "textScore"})]).to_list(1000)

    return [BookInDB(**book, id=str(book["_id"])) for book in result]




# Аггрегация
@router.get("/books/average_price")
async def get_average_book_price(db: AsyncIOMotorDatabase = Depends(get_database)):
    pipeline = [
        {"$group": {"_id": None, "average_price": {"$avg": "$price"}}}
    ]

    result = await db.books.aggregate(pipeline).to_list(1)

    if result and result[0].get("average_price") is not None:
        average_price = result[0]["average_price"]
        return {"average_price": average_price}
    else:
        return {"average_price": 0.0}