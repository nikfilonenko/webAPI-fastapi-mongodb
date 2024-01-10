# routers/__init__.py

from fastapi import APIRouter
from . import book, publisher, product_model

router = APIRouter()

router.include_router(book.router, prefix="/books", tags=["books"])
router.include_router(publisher.router, prefix="/publishers", tags=["publishers"])
router.include_router(product_model.router, prefix="/product_models", tags=["product_models"])
