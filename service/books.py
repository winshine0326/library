from data import books as data
from sqlite3 import IntegrityError

def register_book(title: str, author: str) -> dict:
    try:
        data.register_book(title, author)
        return {"success": True, "message": "도서 등록 완료"}
    except IntegrityError:
        return {"success": False, "message": "이미 존재하는 제목입니다"}

def get_book_list() -> dict:
    try:
        books = data.get_book_list()
        return {"books_list": books}
    except IntegrityError:
        return {"success": False, "message": "리스트가 비어있습니다."}

def delete_book(book_id : int) -> bool:
    try:
        return data.delete_book(book_id)
    except IntegrityError:
        return False