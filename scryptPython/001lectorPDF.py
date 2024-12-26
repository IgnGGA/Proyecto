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

def genDataFrame():
    rutasArchivos=rutasOSTT('OrdenesDeServicioTécnicoAndover/')
    datos=LectorOSSTT(rutasArchivos)
    os.chdir('BaseDeDatos/')
    with open ('DataFrameOrdenesDeServicio','w') as archivo:
        for i in range(len(datos)):
            for j in range(len(datos[i])):
                archivo.write(datos[i][j]+'\n')
genDataFrame()