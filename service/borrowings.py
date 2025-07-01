from sqlite3 import IntegrityError
from typing import List

from data import borrowings as data
from cache import borrower as cache

def borrow_book(borrower: str, title : str) -> bool:
    try:
        cache.add_borrowed_book(borrower, title)
        return data.borrow_book(borrower,title)
    except IntegrityError:
        return False

def get_books_by_month(borrow_month : str) -> List[dict]:
    try:
        return data.get_books_by_month(borrow_month)
    except IntegrityError:
        return {"success":False}

def borrow_history(borrower : str) -> dict:
    try:
        books = cache.get_borrowed_books(borrower)
        return {
            "borrower": borrower,
            "books": books
        }
    except IntegrityError:
        return {"success":False}