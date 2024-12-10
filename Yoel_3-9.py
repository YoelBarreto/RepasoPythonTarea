"""
 Crea un programa Python 3 que organice los archivos de la carpeta actual. 
 Para cada extensión de archivo, el programa moverá todos los archivos con esa extensión a una carpeta con el mismo nombre que la extensión. 
 Por ejemplo, una lista con extensiones [“png”, “mp4”, “doc”] moverá los archivos ".png" a una carpeta "png", los ".mp4" a una carpeta "mp4", 
 y los ".doc" a una carpeta "doc", si no corresponde la extensión ignorar el archivo. Para distribuir el programa, empaquétalo con PyInstaller.
"""

import os
import shutil

def organizar_archivos():
    carpeta_actual = os.getcwd()
    
    for archivo in os.listdir(carpeta_actual):
        if os.path.isfile(archivo):
            nombre, extension = os.path.splitext(archivo)
            
            if extension:
                extension = extension[1:]
                carpeta_destino = os.path.join(carpeta_actual, extension)
                os.makedirs(carpeta_destino, exist_ok=True)
                
                shutil.move(archivo, os.path.join(carpeta_destino, archivo))
                print(f"Movido: {archivo} -> {carpeta_destino}")

if __name__ == "__main__":
    organizar_archivos()