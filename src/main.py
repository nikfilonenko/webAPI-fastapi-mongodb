import uvicorn
from fastapi import FastAPI
from src.routers import book, publisher, product_model
from src.database import connect_to_mongo, close_mongo_connection

app = FastAPI()

app.include_router(book.router)
app.include_router(publisher.router)
app.include_router(product_model.router)

@app.on_event("startup")
async def startup_db_client():
    await connect_to_mongo()

@app.on_event("shutdown")
async def shutdown_db_client():
    await close_mongo_connection()


if __name__ == "__main__":
    uvicorn.run("src.main:app", host="127.0.0.1", port=8000, reload=True)