from app import books

USER_CHOICE = """Enter one of following

- b to look at 5-star books
- c to look at the cheapest books
- n to to just get the next available book on the page
- q to to exit

Enter your choice: """


def print_best_books():
    best_books = sorted(books, key=lambda x: (x.rating, x.price * -1), reverse=True)[:5]
    for book in best_books:
        print(book)


def print_cheapest_books():
    best_books = sorted(books, key=lambda x: x.price)[:5]
    for book in best_books:
        print(book)


books_generator = (x for x in books)


def get_next_book():
    print(next(books_generator))


user_choices = {
    "b": print_best_books,
    "c": print_cheapest_books,
    "n": get_next_book
}


def menu():
    user_input = input(USER_CHOICE)
    while user_input != "q":
        if user_input in user_choices:
            user_choices[user_input]()
        else:
            print("Please choose valid command")

        user_input = input(USER_CHOICE)


menu()
