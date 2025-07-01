from fastapi import APIRouter
from service import books as books_service
from pydantic import BaseModel

class BookIn(BaseModel):
    title: str
    author: str

router = APIRouter(prefix="/books")

@router.post("")
def register_book(book: BookIn):
    return books_service.register_book(book.title,book.author)