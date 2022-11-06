from PyPDF2 import PdfReader, PdfWriter

template = PdfReader("merged.pdf")
watermark = PdfReader("wtr.pdf")

writer = PdfWriter()

for page in template.pages:
    page.merge_page(watermark.pages[0])
    writer.add_page(page)

writer.write("watermarked.pdf")
