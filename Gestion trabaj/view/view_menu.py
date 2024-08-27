import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
# from .trabaj import insertar_trab, list_trabj
from .view_trabaj import *
from .view_workdate import *
from .view_dateactive import *
from .rep_periodo import *
from .common import *


class AplicacionMenu:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistena de registro")

        # Crear la barra de menú
        self.menu_bar = tk.Menu(self.root)

        # Crear el menú Archivo
        self.archivo_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.archivo_menu.add_command(
            label="Agregar Trabajadores", command=self.nuevo_archivo)
        self.archivo_menu.add_command(
            
            label="Agregar asistencia", command=self.abrir_archivo)
        self.archivo_menu.add_separator()
        self.archivo_menu.add_command(label="Salir", command=self.salir)

        # Agregar el menú Archivo a la barra de menú
        self.menu_bar.add_cascade(label="Archivo", menu=self.archivo_menu)
        
        
        self.gestion_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.gestion_menu.add_command(
            label="Fecha Periodo", command=self.date_work)
        
        
        self.menu_bar.add_cascade(label="Gestion", menu=self.gestion_menu)
        
        
        self.reporte_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.reporte_menu.add_command(
            label="Reporte Periodo", command=self.reportes_periodo)
        
        
        self.menu_bar.add_cascade(label="Reportes", menu=self.reporte_menu)
        
        # Configurar la barra de menú en la ventana principal
        self.root.config(menu=self.menu_bar)
        
        # Centrar la ventana usando la nueva clase
        centrar = CentrarVentana(self.root)
        centrar.centrar()


    def nuevo_archivo(self):

        NuevoTrabajadorVentana(self.root)

    def abrir_archivo(self):
        NuevoDatWorkVentana(self.root)

        #messagebox.showinfo("Abrir", "Archivo abierto")
        
    def date_work(self):
        NuevodateActive(self.root)
        
    def reportes_periodo(self):
        #messagebox.showinfo("Abrir", "Falta por hacer el reporte")
        reportes_rango = ReportesRango()
        reportes_rango.list_rangofecha()
        #print (f'{muestras()} y {trabaja} ')
        #NuevodateActive(self.root)

    def salir(self):
        self.root.quit()
