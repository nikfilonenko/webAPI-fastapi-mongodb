from fastapi import FastAPI
from posts import router
from database import connect_to_mongo, close_mongo_connection

app = FastAPI()

app.include_router(books.router)
app.include_router(publishers.router)

@app.on_event("startup")
async def startup_db_client():
    await connect_to_mongo()

@app.on_event("shutdown")
async def shutdown_db_client():
    await close_mongo_connection()
