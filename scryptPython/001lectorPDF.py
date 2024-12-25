from pdfquery import PDFQuery
pdf = PDFQuery('OrdenesDeTrabajoTrilogy/202401/Orden de servicio técnico Andover.118924-287932.pdf')
pdf.load()
text_elements = pdf.pq('LTTextLineHorizontal')
text = [t.text for t in text_elements]
print(text)

i=0
dim=len(text)

for i in range(dim):
    print(len(text))
    if text[i]=='':
        text.pop(i)
        dim=len(text)
    
print(text)