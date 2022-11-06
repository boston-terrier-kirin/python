import sys
from PyPDF2 import PdfReader, PdfMerger

# 02_merge.py twopage.pdf dummy.pdf -----> merged.pdf
inputs = sys.argv[1:]


def pdf_combiner(pdf_list):
    merger = PdfMerger()
    for pdf in pdf_list:
        number_of_pages = len(merger.pages)
        merger.merge(number_of_pages, PdfReader(pdf))

        print(pdf, f"added at page index: {number_of_pages}")

    merger.write("merged.pdf")


pdf_combiner(inputs)
