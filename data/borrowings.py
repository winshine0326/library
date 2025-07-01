from . import con, cur
from typing import List

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

def get_books_by_month(borrow_month) -> List[dict]:
    sql = """
            SELECT b.borrower, bo.title, bo.author
            FROM borrowings b
            JOIN books bo ON b.book_id = bo.book_id
            WHERE strftime('%Y-%m', b.borrowed_at) = ?
        """
    cur.execute(sql, (borrow_month,))
    rows = cur.fetchall()
    return [{"borrower": row[0], "title": row[1], "author": row[2]} for row in rows]


def delete_borrowing(borrower: str) -> bool:
    cur.execute("""
                DELETE FROM borrowings
                WHERE borrower = ?
            """, (borrower,))
    con.commit()
    return True


def set_book_available(title: str) -> bool:
    cur.execute("""
        UPDATE books
        SET available = 1
        WHERE title = ?
    """, (title,))
    con.commit()
    return True

def is_book_already_borrowed(title: str) -> bool:
    cur.execute("""
        SELECT 1
        FROM borrowings b
        JOIN books bo ON b.book_id = bo.book_id
        WHERE bo.title = ? AND b.returned_at IS NULL
        LIMIT 1
    """, (title,))
    return cur.fetchone() is not None