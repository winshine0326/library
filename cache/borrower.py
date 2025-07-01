from . import redis_client

def add_borrowed_book(borrower: str, title: str):
    key = f"borrower:{borrower}:books"
    redis_client.lpush(key, title)

def get_borrowed_books(borrower: str):
    key = f"borrower:{borrower}:books"
    return redis_client.lrange(key, 0, -1)

def clear_borrowed_books(borrower: str):
    key = f"borrower:{borrower}:books"
    redis_client.delete(key)