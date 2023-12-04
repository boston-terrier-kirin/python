from fastapi import FastAPI, Body

app = FastAPI()

BOOKS = [
    {"title": "Title One", "author": "Author One", "category": "science"},
    {"title": "Title Two", "author": "Author Two", "category": "science"},
    {"title": "Title Three", "author": "Author Three", "category": "history"},
    {"title": "Title Four", "author": "Author Four", "category": "history"},
    {"title": "Title Five", "author": "Author Five", "category": "math"},
    {"title": "Title Six", "author": "Author Six", "category": "math"},
]


@app.get("/books")
async def read_all_books():
    print("read_all_books")
    return BOOKS


@app.get("/books/{book_title}")
async def read_book(book_title: str):
    print("read_book")

    for book in BOOKS:
        if book.get("title").casefold() == book_title.casefold():
            return book

    return {}


@app.get("/books/")
async def read_category_by_query(category: str):
    books_to_return = [book for book in BOOKS if book.get("category").casefold() == category.casefold()]
    return books_to_return


@app.get("/books/{book_author}/")
def read_author_category_by_query(book_author: str, category: str):
    print("read_author_category_by_query")

    books_to_return = []
    for book in BOOKS:
        if book.get("author").casefold() == book_author.casefold() and \
                book.get("category").casefold() == category.casefold():
            books_to_return.append(book)

    return books_to_return


@app.post("/books/create_book")
async def create_new_book(new_book=Body()):
    BOOKS.append(new_book)


@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    for index, book in enumerate(BOOKS):
        if book.get("title").casefold() == updated_book.get("title").casefold():
            BOOKS[index] = updated_book


@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for index, book in enumerate(BOOKS):
        if book.get("title").casefold() == book_title.casefold():
            BOOKS.pop(index)
            break
