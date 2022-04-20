import os
from pathlib import Path

if not os.path.exists(f'./archivos'):
    os.makedirs(f'./archivos')

file = open("./archivos/filename.txt", "w")
file.write("Primera línea" + os.linesep)
file.write("Segunda línea")
file.close()

print("Ruta Directorio actual: ", Path.cwd())