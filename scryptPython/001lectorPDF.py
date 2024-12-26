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

def LectorOSSTT(rutaArchivos):
    dataOSSTT=[]
    for i in range(len(rutaArchivos)):
        pdf = PDFQuery(rutaArchivos[i])
        pdf.load()
        text_elements = pdf.pq('LTTextLineHorizontal')
        text = [t.text for t in text_elements]
        dataOSSTT.append(text)
    return dataOSSTT

rutasArchivos=rutasOSTT('OrdenesDeServicioTécnicoAndover/')
print(f'Tipo de dato:\t{type(rutasArchivos)}\nTamaño del dato:\t{len(rutasArchivos)}')
datos=LectorOSSTT(rutasArchivos)
print(f'Tipo de dato:\t{type(datos)}\nTamaño del dato:\t{len(datos)}')