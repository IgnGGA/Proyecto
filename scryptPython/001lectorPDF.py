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

rutasArchivos=rutasOSTT('OrdenesDeServicioTécnicoAndover/')
print(rutasArchivos)
print(f'Tipo de dato:\t{type(rutasArchivos)}\nTamaño del dato:\t{len(rutasArchivos)}')