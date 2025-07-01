from fastapi import FastAPI

from web import borrowings as borrow_web
from web.books import router as book_web
from service import borrowings as borrow_service

app = FastAPI()
app.include_router(borrow_web.router)
app.include_router(book_web)

@app.post("return")
def return_book(borrower : str, title : str) -> bool:
    return borrow_service.return_book(borrower, title)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host='0.0.0.0', reload=True)
