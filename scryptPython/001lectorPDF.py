from pdfquery import PDFQuery
pdf = PDFQuery('OrdenesDeTrabajoTrilogy/202401/Orden de servicio técnico Andover.118924-287932.pdf')
pdf.load()
text_elements = pdf.pq('LTTextLineHorizontal')
text = [t.text for t in text_elements]
print(text)

a,b=0,0
dim=len(text)

while True:
    try:
        for a in range (dim):
            print(len(text))
            if text[a]=='' or text[a]==' ':
                text.pop(a)
        break
    except IndexError:
        b=b+1
        print(f'Fin iteración:\t{b}')
print(text)