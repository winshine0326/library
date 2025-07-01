from . import con, cur

def register_book(title: str, author: str):
    sql = "INSERT INTO books (title, author) VALUES (?, ?)"
    cur.execute(sql, (title, author))
    con.commit()

def get_book_list():
    sql = "SELECT title, author FROM books"
    cur.execute(sql)
    rows = cur.fetchall()
    return [{"title": row[0], "author": row[1]} for row in rows]