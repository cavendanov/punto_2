import os
import PyPDF2
import re
import sqlite3 as sql

def checkFile(fileName):
    file = open("pdf/" + fileName, "rb")
    try:
        pdf = PyPDF2.PdfReader(file)
        info = pdf.metadata
        if info:
            return True
        else:
            return False
    except Exception as e:
        return False


def pdfNumberOfPages(fileObject):
    read_pdf = PyPDF2.PdfReader(fileObject)
    return len(read_pdf.pages)

def pdfGetCUFE(fileObject):
    reader = PyPDF2.PdfReader(fileObject)
    page = reader.pages[0]
    text = page.extract_text()
    pattern = r'(\b([0-9a-fA-F]\n*){95,100}\b)'
    return re.search(pattern, text)

def getSize(fileobject):
    fileobject.seek(0,2)
    size = fileobject.tell()
    return size

def createDB():
    conn = sql.connect("db/punto_2.db")
    cursor = conn.cursor()
    query = f"SELECT name FROM sqlite_master WHERE type = 'table' AND name='facturas'"
    cursor.execute(query)
    result = cursor.fetchone()
    if result:
        conn.close()
    else:    
        cursor.execute(
            """CREATE TABLE facturas(
                nombre text,
                numero_paginas integer,
                cufe text,
                peso integer
            )"""
        )
        conn.commit()
        conn.close()

def insertRow(fileName, numberOfPages, cufe, peso):
    conn = sql.connect("db/punto_2.db")
    cursor = conn.cursor()
    query = f"SELECT COUNT(*) FROM facturas where nombre = '{fileName}'"
    cursor.execute(query)
    count = cursor.fetchone()[0]
    if count > 0:
        query = f"UPDATE facturas SET numero_paginas = {numberOfPages}, cufe = '{cufe}', peso = {peso} WHERE nombre = '{fileName}'"
        cursor.execute(query)
        conn.commit()
        conn.close()
        print("Archivo actualizado correctamente")
    else:
        query = f"INSERT INTO facturas VALUES ('{fileName}', {numberOfPages}, '{cufe}', {peso})"
        cursor.execute(query)
        conn.commit()
        conn.close()
        print("Archivo ingresado correctamente")

#Creación de la base de datos y la tabla de facturas
createDB()
#Solicita el nombre del archivo
fileName = input("Hola. Introduce el nombre del archivo: ")
#verifica que el archivo existe
existFile = os.path.exists("pdf/" + fileName)
if existFile:
    file = open("pdf/" + fileName, "rb")
    #Valida que el archivo sea PDF
    checkedFile = checkFile(fileName)
    if checkedFile:
        #Obtener el peso del archivo
        weight = getSize(file)
        #Obtener el número de páginas del archivo
        numberOfPages = pdfNumberOfPages(file)
        #Obtener el CUFE
        cufe = pdfGetCUFE(file)
        #Guardar o actualizar el registro dependiendo del nombre del archivo
        insertRow(fileName, numberOfPages, cufe.group(), weight)
    else:
        print("Archivo no valido")
else:
    print("Archivo no encontrado")

