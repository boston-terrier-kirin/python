from typing import Optional

from fastapi import FastAPI, Path, Query, HTTPException
from pydantic import BaseModel, Field
from starlette import status

app = FastAPI()


class Book:
    id: int
    title: str
    author: str
    desc: str
    rating: int
    published_date: int

    def __init__(self, id, title, author, desc, rating, published_date):
        self.id = id
        self.title = title
        self.author = author
        self.desc = desc
        self.rating = rating
        self.published_date = published_date


class BookRequest(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    desc: str = Field(min_length=3, max_length=100)
    rating: int = Field(gt=0, lt=6)
    published_date: int = Field(gt=1999, lt=2031)

    class Config:
        json_schema_extra = {
            "example": {
                "title": "A new book",
                "author": "Kohei Matsumoto",
                "desc": "A new desc",
                "rating": 4,
                "published_date": 2023
            }
        }


BOOKS = [
    Book(1, "Node", "Kohei", "Your first Node app", 5, 2016),
    Book(2, "FastAPI", "Kirin", "Your first FastAPI app", 4, 2023),
    Book(3, "Springframework", "Kuroro", "Your first Springframework app", 2, 2018),
    Book(4, "Python Basics", "Kohei", "Your first Python app", 5, 2021),
    Book(5, "React Fundamentals", "Kohei", "Your first React app", 5, 2021)
]


@app.get("/books", status_code=status.HTTP_200_OK)
async def read_all_books():
    return BOOKS


@app.get("/books/{book_id}", status_code=status.HTTP_200_OK)
async def read_book(book_id: int = Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book

    raise HTTPException(status_code=404, detail="Item not found.")


@app.get("/books/", status_code=status.HTTP_200_OK)
async def read_book_by_rating(book_rating: int = Query(gt=0, lt=6)):
    return [book for book in BOOKS if book.rating == book_rating]


@app.get("/books/publish/", status_code=status.HTTP_200_OK)
async def read_book_by_published_date(published_date: int = Query(gt=1999, lt=2031)):
    return [book for book in BOOKS if book.published_date == published_date]


@app.post("/create-book", status_code=status.HTTP_201_CREATED)
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    BOOKS.append(find_book_id(new_book))


def find_book_id(book: Book):
    if len(BOOKS) > 0:
        book.id = BOOKS[-1].id + 1
    else:
        book.id = 1

    return book


@app.put("/books/update_book", status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book_request: BookRequest):
    for index, book in enumerate(BOOKS):
        if book.id == book_request.id:
            BOOKS[index] = book_request
            return

    raise HTTPException(status_code=404, detail="Item not found.")


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int = Path(gt=0)):
    for index, book in enumerate(BOOKS):
        if book.id == book_id:
            BOOKS.pop(index)
            return

    raise HTTPException(status_code=404, detail="Item not found.")
