import pikepdf

old_pdf = pikepdf.Pdf.open("")      # add path 

for page in old_pdf.pages:
    page.Rotate = 180
    old_pdf.save("Rotated.pdf")