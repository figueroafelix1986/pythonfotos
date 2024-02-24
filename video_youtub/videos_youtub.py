import pytube
import requests
from tqdm import tqdm

video_url = input("Escriba o copie la url: ")

video = pytube.YouTube(video_url)
stream = video.streams.get_highest_resolution()

# Obtener el tamaño del video en bytes
total_size = stream.filesize

# Descargar el video en bloques y mostrar la barra de progreso
response = requests.get(stream.url, stream=True)
with open(f"{video.title}.mp4", "wb") as file:
    with tqdm(total=total_size, unit='B', unit_scale=True, unit_divisor=1024) as pbar:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                file.write(chunk)
                pbar.update(len(chunk))

print("Video descargado bien")