from pdfquery import PDFQuery
import os

def rutasOSTT(directorio):
    rutas=[]
    while True:
        try:
            for root, dirs, files in os.walk(directorio):
                for file in files:
                    if file.endswith('.pdf'):
                        rutas.append(os.path.join(root, file))
            break
        except FileNotFoundError:
            print('Directorio no encontrado')
            break
    return rutas

rutasOSTT('OrdenesDeServicioTécnicoAndover')

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
            if text[-a]=='' or text[-a]==' ':
                text.pop(-a)
        break
    except IndexError:
        b=b+1
        print(f'Fin iteración:\t{b}')
print(text)