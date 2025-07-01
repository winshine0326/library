from sqlite3 import IntegrityError

from data import borrowings as data
from cache import borrower as cache

def borrow_book(borrower: str, title : str) -> bool:
    try:
        cache.add_borrowed_book(borrower, title)
        return data.borrow_book(borrower,title)
    except IntegrityError:
        return False