import requests
import logging
from pages.all_books_page import AllBooksPage

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s",
                    filename="app.log")
logger = logging.getLogger("book_logger")

page_content = requests.get("https://books.toscrape.com/").content
page = AllBooksPage(page_content)

books = page.books

for page_num in range(1, page.page_count):
    url = f"https://books.toscrape.com/catalogue/page-{page_num + 1}.html"
    logger.info(url)
    page_content = requests.get(url).content
    page = AllBooksPage(page_content)
    books.extend(page.books)
