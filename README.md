
# Prueba Técnica para Desarrollador Senior ADRES - 2025 - Punto2

Cree un script en Python que extraiga la información del CUFE con la siguiente expresión regular *(\b([0-9a-fA-F]\n*){95,100}\b)* de los archivos. Almacene el resultado en una base de datos SQLite con la siguiente información: Nombre del archivo, Numero de paginas, CUFE, Peso del archivo


## Features

- Los archivos PDF deben estar cargados en la carpeta pdf
- Crear la base de datos y la tabla en la carpeta db
- Cuando se iniciaiza el script se solicita al usuario el nombre del archivo
- El script valida que el archivo existe
- El script valida que el archivo sea pdf
- Toma la información de peso del archivo, número de páginas y CUFE
- El script procesa el archivo y crea un nuevo registro en la tabla
- Si el archivo ya fue procesado con anterioridad, se actualiza el registro de la base de datos


## Documentation

- Desde la terminal del computador dirigirse a la carpeta donde se descargaron los archivos
- Ejecutar el comando python3 punto2_py


## Tech Stack

- Python
- SQLite3

Librerías utilizadas
- os
- PyPDF2
- re
- sqlite3

