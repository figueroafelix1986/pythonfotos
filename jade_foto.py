import os
import shutil
import glob
from pathlib import Path
from tkinter import filedialog
from PIL import Image


def select_folder():
    """
    Función que muestra un diálogo para seleccionar una carpeta
    y retorna la ruta de la carpeta seleccionada.
    Si el usuario no selecciona ninguna carpeta, la función sale del programa.
    """
    folder_selected = filedialog.askdirectory()
    if not folder_selected:
        exit()
    return folder_selected


def get_files_from_folder(folder_selected, pattern):
    """
    Función que recibe la ruta de una carpeta y un patrón de búsqueda,
    y retorna una lista de rutas de los archivos que coinciden con el patrón.
    """
    return glob.glob(os.path.join(folder_selected, pattern))


def extract_year_month(filename, start, end):
    """
    Función que recibe el nombre de un archivo y dos índices
    que indican el inicio y fin de la subcadena a extraer del nombre del archivo.
    Retorna la subcadena extraída.
    """
    return filename[start:end]


def organize_images(folder_selected):
    """
    Función que recibe la ruta de una carpeta y mueve las imágenes
    que coinciden con los patrones definidos a una estructura de carpetas
    organizada por año y mes.
    """
    image_patterns = ['IMG_*', 'IMG-*']
    for pattern in image_patterns:
        files = get_files_from_folder(folder_selected, pattern)
        for file in files:
            filename = os.path.split(file)[1]
            year = extract_year_month(filename, 4, 8)
            month = extract_year_month(filename, 8, 10)
            destination = os.path.join("Fotos", year, f"{year}{month}")
            os.makedirs(destination, exist_ok=True)
            picture = Image.open(file)
            picture.save(os.path.join(destination, filename),
                        optimize=True, quality=60)
            os.remove(file)


def organize_videos(folder_selected):
    """
    Función que recibe la ruta de una carpeta y mueve los videos
    que coinciden con los patrones definidos a una estructura de carpetas
    organizada por año y mes.
    """
    video_patterns = ['VID_*', 'VID-*']
    for pattern in video_patterns:
        files = get_files_from_folder(folder_selected, pattern)
        for file in files:
            filename = Path(file).stem
            year = extract_year_month(filename, 4, 8)
            month = extract_year_month(filename, 8, 10)
            destination = os.path.join("Videos", year, f"{year}{month}")
            os.makedirs(destination, exist_ok=True)
            shutil.copy2(file, destination)
            os.remove(file)


def main():
    """
    Función principal que llama a las funciones para organizar las imágenes y videos
    en una estructura de carpetas organizada por año y mes.
    """
    folder_selected = select_folder()
    organize_images(folder_selected)
    organize_videos(folder_selected)


if __name__ == "__main__":
    main()
