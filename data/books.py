from . import con, cur

def register_book(title: str, author: str):
    sql = "INSERT INTO books (title, author) VALUES (?, ?)"
    cur.execute(sql, (title, author))
    con.commit()