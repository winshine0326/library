from data import books as data
from sqlite3 import IntegrityError

def register_book(title: str, author: str) -> dict:
    try:
        data.register_book(title, author)
        return {"success": True, "message": "도서 등록 완료"}
    except IntegrityError:
        return {"success": False, "message": "이미 존재하는 제목입니다"}