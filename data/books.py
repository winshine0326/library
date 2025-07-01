from . import con, cur

def register_book(title: str, author: str) -> bool:
    sql = "INSERT INTO books (title, author) VALUES (?, ?)"
    cur.execute(sql, (title, author))
    con.commit()
    return True

def get_book_list():
    sql = "SELECT title, author FROM books"
    cur.execute(sql)
    rows = cur.fetchall()
    return [{"title": row[0], "author": row[1]} for row in rows]


def delete_book(book_id : int) -> bool:
    sql = "DELETE FROM books where book_id=(?)"
    cur.execute(sql, (str(book_id),))
    con.commit()
    return True