import imaplib
import sys, os
from distutils.util import execute
import shutil
from time import sleep
import keyboard
from glob import glob
import datetime
import win32console
import win32gui


"""ventana = win32console.GetConsoleWindow()
win32gui.ShowWindow(ventana,0)"""

#Copiar en un archivo de texto las trazas 
def trazas_fichero(fecha, i,destino_fin):
    file = open(destino_fin +"productos_trazas.txt", "a")
    file.write(str(fecha) + "----"+ i + os.linesep)
    file.close()

#katapul
def extraer_ann_mes (i,n=14):
    return i[8:n]


def extraer_ann (i,n=12):
    return i[8:n]

def extraer_inicio (i,n=14):
    return i[0:n]


def extraer_dia (i,n=16):
    return i[14:n]

def extraer_final (i,n):
    return i[16:n]

#delchef
def delchef_ann_mes (i,n=32):
    return i[25:n]

def delche_ann (i,n=29):
    return i[25:n]

#imprimir despacho katapul

def despachokat_ann_mes (i,n=14):
    return i[8:n]

def despachokat_ann (i,n=12):
    return i[8:n]

#imprimir despacho super mark

def despachoDchef_ann_mes (i,n=33):
    return i[26:n]

def despachoDchef_ann (i,n=30):
    return i[26:n]

#retorna todos los valores que tengan los parametros que puse
def litar_archivo(desde_inicio):
    listar=glob(desde_inicio)
    return listar
    





print ("Lista de movimientos")    

while True:
  sleep(5)

  date = datetime.date.today()
  year = date.strftime("%Y")
  fecha = datetime.datetime.now()

  
  #KATAPUL
  try:

    desde_inicio = 'pedidos*_productos*.xls'    
    resultado =litar_archivo(desde_inicio)
  
    for i in resultado:          
        anno_mes_fich = extraer_ann_mes (i)
        os.path.join(anno_mes_fich)
        anno_fich = extraer_ann (i)
        os.path.join(anno_fich)
        destino_fin = "D:/YOYO/KATAPULK/"+anno_fich+"/"+anno_mes_fich
        os.path.join(destino_fin)
        os.makedirs(destino_fin, exist_ok=True)
        print(i)
        trazas_fichero(fecha, i,destino_fin)
        inicio = extraer_inicio(i)  
        dia = extraer_dia(i)  
        final = extraer_final(i,len(i))
        nuevo_nombre = f"{inicio}-{dia}-{final}"
        os.rename(i,nuevo_nombre)
        shutil.copy2(nuevo_nombre,destino_fin)
        os.remove(nuevo_nombre)
        
        
    if keyboard.is_pressed('Esc'):
        sys.exit()
       
  except Exception as e:
    pass


#Super marquer
  try:

    delchef_inicio = '*TKC_vale_entrega_Delchef*'    
    delchef_resultado =litar_archivo(delchef_inicio)
    
  
    for j in delchef_resultado:          
        anno_mes_fich =delchef_ann_mes (j)
        os.path.join(anno_mes_fich)
        anno_fich = delche_ann (j)
        os.path.join(anno_fich)
        supermark_fin = "D:/YOYO/Super_Market23/"+anno_fich+"/"+anno_mes_fich
        os.path.join(supermark_fin)
        os.makedirs(supermark_fin, exist_ok=True)
        print(j)
        trazas_fichero(fecha, j,supermark_fin)
        shutil.copy2(j,supermark_fin)
        os.remove(j)
        
    if keyboard.is_pressed('Esc'):
        sys.exit()
       
  except Exception as e:
    pass


#Imprimir despacho katapul
  try:

    despachoKat_inicio = 'ordenes_*'    
    despachoKat_resultado =litar_archivo(despachoKat_inicio)
    
  
    for k in despachoKat_resultado:          
        anno_mes_fich =despachokat_ann_mes (k)
        os.path.join(anno_mes_fich)
        anno_fich = despachokat_ann (k)
        os.path.join(anno_fich)
        despachokat_fin = "D:/YOYO/Despacho_Katapul/"+anno_fich+"/"+anno_mes_fich
        os.path.join(despachokat_fin)
        os.makedirs(despachokat_fin, exist_ok=True)
        print(k)
        trazas_fichero(fecha, k,despachokat_fin)
        shutil.copy2(k,despachokat_fin)
        os.remove(k)
        
    if keyboard.is_pressed('Esc'):
        sys.exit()
       
  except Exception as e:
    pass



#Imprimir despacho Super Marker
  try:

    despachoDchef_inicio = 'TKC_despacho_Delchef_*'    
    despachoDchef_resultado =litar_archivo(despachoDchef_inicio)
    
  
    for z in despachoDchef_resultado:          
        anno_mes_fich =despachoDchef_ann_mes (z)
        os.path.join(anno_mes_fich)
        anno_fich = despachoDchef_ann (z)
        os.path.join(anno_fich)
        despachoDchef_fin = "D:/YOYO/Despacho_SuperMark/"+anno_fich+"/"+anno_mes_fich
        os.path.join(despachoDchef_fin)
        os.makedirs(despachoDchef_fin, exist_ok=True)
        print(z)
        trazas_fichero(fecha, z,despachoDchef_fin)
        shutil.copy2(z,despachoDchef_fin)
        os.remove(z)
        
    if keyboard.is_pressed('Esc'):
        sys.exit()
       
  except Exception as e:
    pass


#Eliminar KATAPULK
  try:

    pedidos_info = 'pedidos_*_info*'    
    kata_para_elimi =litar_archivo(pedidos_info)
    
  
    for j in kata_para_elimi:      
        os.remove(j)
        
    if keyboard.is_pressed('Esc'):
        sys.exit()
       
  except Exception as e:
    pass


