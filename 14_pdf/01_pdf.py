# https://pypi.org/project/PyPDF2/
from PyPDF2 import PdfReader, PdfWriter

reader = PdfReader("dummy.pdf")
number_of_pages = len(reader.pages)

page = reader.pages[0]
text = page.extract_text()

print("number_of_pages", number_of_pages)
print("text", text)

# rotate
page.rotate_clockwise(90)

writer = PdfWriter()
writer.add_page(page)
writer.write("rotate.pdf")
