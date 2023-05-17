import imaplib
import sys, os
from distutils.util import execute
import shutil
from time import sleep
import keyboard
import glob
import datetime
import win32console
import win32gui
from PIL import Image
from tkinter import filedialog
from pathlib import Path

folder_selected = filedialog.askdirectory()

if not folder_selected:
    exit()

file_list = glob.glob(folder_selected)



for file in file_list:
    carpeta_list = file
    
#retorna todos los valores que tengan los parametros que puse
def litar_archivo(desde_inicio):
    listar=glob.glob(desde_inicio)
    return listar

def extraer_ann_mes (i,n=10):
    return i[4:n]

def extraer_ann (i,n=8):
    return i[4:n]

def extraer_ann_2 (i,n=4):
    return i[0:n]

def extraer_ann_mes_2 (i,n=6):
    return i[0:n]

list_destino = ['IMG_*', 'IMG-*']

for desde_inicio in list_destino:
    try:
        
     desde_inicio=carpeta_list+'/'+desde_inicio
     
     resultado =litar_archivo(desde_inicio)
     for img_fichero in resultado:
       
        #imagen_fichero = Path(img_fichero).stem
        imagen_fichero=os.path.split(img_fichero)
        imagen_fichero=imagen_fichero[1]
        
        
        destino_fin ="Fotos/"+os.path.join(extraer_ann(imagen_fichero)) +"/"+os.path.join(extraer_ann_mes(imagen_fichero))
        
       
        os.makedirs(destino_fin, exist_ok=True)
        
        picture=Image.open(img_fichero)
        
       
        picture.save(destino_fin+'/'+imagen_fichero,optimize= True, quality=60)
        #shutil.copy2(img_fichero,destino_fin)
        print (imagen_fichero)
        os.remove(img_fichero)
        #shutil.copy2(i,destino_fin)
        
    except Exception as e:
     pass

desde_inicio='*.jpg'

try:
     desde_inicio=carpeta_list+'/'+desde_inicio
        
     resultado =litar_archivo(desde_inicio)
     for img_fichero in resultado:      
         
        #imagen_fichero = Path(img_fichero).stem
        imagen_fichero=os.path.split(img_fichero)
        imagen_fichero=imagen_fichero[1]
        
        
        destino_fin ="Fotos/"+os.path.join(extraer_ann_2(imagen_fichero)) +"/"+os.path.join(extraer_ann_mes_2(imagen_fichero))
        os.makedirs(destino_fin, exist_ok=True)
        picture=Image.open(img_fichero)
        
        picture.save(destino_fin+'/'+imagen_fichero,optimize= True, quality=60)
        #shutil.copy2(img_fichero,destino_fin)
        print (imagen_fichero)
        os.remove(img_fichero)
        #shutil.copy2(i,destino_fin)
        
except Exception as e:
     pass
 
#PARA MOVER LOS VIDEOS


list_destino = ['VID_*', 'VID-*']

for desde_inicio in list_destino:
    try:
     
     desde_inicio=carpeta_list+'/'+desde_inicio   
     resultado =litar_archivo(desde_inicio)    
     for vid_fichero in resultado:
        
      
        
        video_fichero = Path(vid_fichero).stem
        
        
        
        destino_fin ="Videos/"+os.path.join(extraer_ann(video_fichero)) +"/"+os.path.join(extraer_ann_mes(video_fichero))
        os.makedirs(destino_fin, exist_ok=True)
        #picture=Image.open(imagen_fichero)
        shutil.copy2(vid_fichero,destino_fin)
        print (video_fichero)
        os.remove(vid_fichero)
        #shutil.copy2(i,destino_fin)
        
    except Exception as e:
     pass
 
 
desde_inicio='*.mp4'

try:
     desde_inicio=carpeta_list+'/'+desde_inicio
        
     resultado =litar_archivo(desde_inicio)
     for vid_fichero in resultado:      
         
        video_fichero = Path(vid_fichero).stem
        
        destino_fin ="Videos/"+os.path.join(extraer_ann_2(video_fichero)) +"/"+os.path.join(extraer_ann_mes_2(video_fichero))
        os.makedirs(destino_fin, exist_ok=True)
        #picture=Image.open(video_fichero)
        #picture=picture.rotate(270, expand=True)
        shutil.copy2(vid_fichero,destino_fin)
        print (video_fichero)
        os.remove(vid_fichero)
        #shutil.copy2(i,destino_fin)
        
except Exception as e:
     pass