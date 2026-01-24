from pypdf import PdfWriter
import os

merge = PdfWriter()


files = [pdf for pdf in os.listdir() if pdf.endswith(".pdf")]

for pdf in files:
    merge.append(files)

merge.write("Mergedpdf.pdf")
merge.close()