from . import con, cur


def borrow_book(borrower : str, title : str) -> bool:
    cur.execute("SELECT book_id, available FROM books WHERE title = ?", (title,))
    row = cur.fetchone()
    if row is None:
        return False

    book_id, available = row
    if available == 0:
        return False

    cur.execute(
        "INSERT INTO borrowings (book_id, borrower) VALUES (?, ?)",
        (book_id, borrower)
    )
    cur.execute(
        "UPDATE books SET available = 0 WHERE book_id = ?",
        (book_id,)
    )
    con.commit()
    return True
