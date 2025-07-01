from sqlite3 import IntegrityError
from typing import List

from data import borrowings as data
from cache import borrower as cache

def borrow_book(borrower: str, title : str) -> bool:
    try:
        if data.is_book_already_borrowed(title):
            return False
        cache.add_borrowed_book(borrower, title)
        return data.borrow_book(borrower,title)
    except IntegrityError:
        return False

def get_books_by_month(borrow_month : str) -> List[dict]:
    try:
        return data.get_books_by_month(borrow_month)
    except IntegrityError:
        return [{"success":False}]

def borrow_history(borrower : str) -> dict:
    try:
        books = cache.get_borrowed_books(borrower)
        return {
            "borrower": borrower,
            "books": books
        }
    except IntegrityError:
        return {"success":False}

def return_book(borrower : str, title : str) -> bool:
    try:
        update_borrow = data.delete_borrowing(borrower)
        available_borrow = data.set_book_available(title)
        return available_borrow and update_borrow
    except IntegrityError:
        return False
