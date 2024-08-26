import tkinter as tk
from tkinter import ttk, messagebox
#from .datework import insertar_trab, list_trabj, eliminar_trab, actualizar_trab
from .common import *


class NuevoDatWorkVentana:
    def __init__(self, root):
        self.root = root
        self.font= ("Arial", 12)
        self.nueva_ventana = tk.Toplevel(self.root)
        self.nueva_ventana.title("Datos de trabajadores")

        # Ocultar la ventana principal
        self.root.withdraw()
        # Configurar el evento de cierre de la nueva ventana
        self.nueva_ventana.protocol("WM_DELETE_WINDOW", self.on_close)

        # Crear etiquetas y campos de entrada
        tk.Label(self.nueva_ventana, text="Nombre:", font=self.font).grid(
            row=0, column=0, padx=10, pady=5)
        self.nombre_combobox = ttk.Combobox(self.nueva_ventana, font=self.font)
        self.nombre_combobox['values'] = ("Opción 1", "Opción 2", "Opción 3")  # Añadir opciones
        self.nombre_combobox.grid(row=0, column=1, padx=10, pady=5)

        self.nombre_combobox.bind('<KeyRelease>', self.autocompletar)
        
        
        
        tk.Label(self.nueva_ventana, text="Apellidos:", font=self.font).grid(
            row=1, column=0, padx=10, pady=5)
        self.apellidos_entry = tk.Entry(self.nueva_ventana, font=self.font)
        self.apellidos_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.nueva_ventana, text="Salario:", font=self.font).grid(
            row=2, column=0, padx=10, pady=5)
        self.salario_entry = tk.Entry(self.nueva_ventana, font=self.font)
        self.salario_entry.grid(row=2, column=1, padx=10, pady=5)

        # Crear checkbox para activo
        self.activo_var = tk.BooleanVar(value=True)
        self.activo_checkbox = tk.Checkbutton(
            self.nueva_ventana, text="Activo", variable=self.activo_var)
        self.activo_checkbox.grid(row=3, columnspan=2, pady=5)
        
        
        centrar=CentrarVentana(self.nueva_ventana)
        centrar.centrar()

        # Crear un botón Guardar en la nueva ventana
    

        # Botón Guardar
        self.boton_guardar = tk.Button(
            self.nueva_ventana, text="Guardar", command=self.guardar_archivo, font=("Arial", 10), padx=2, pady=2)
        self.boton_guardar.grid(row=1, column=2, pady=10, padx=5, sticky="ew")

        # Botón Eliminar
        self.boton_eliminar = tk.Button(
            self.nueva_ventana, text="Eliminar", command=self.eliminar_archivo, font=("Arial", 10), padx=2, pady=2)
        self.boton_eliminar.grid(row=2, column=2, pady=10, padx=5, sticky="ew")

        # Botón Actualizar
        self.boton_actualizar = tk.Button(
            self.nueva_ventana, text="Actualizar", command=self.actualizar_archivo, font=("Arial", 10), padx=2, pady=2)
        self.boton_actualizar.grid(row=3, column=2, pady=10, padx=5, sticky="ew")
        
        
        
    def on_close(self):
        # Mostrar la ventana principal nuevamente
        self.root.deiconify()
        # Cerrar la ventana actual
        self.nueva_ventana.destroy()
        
    def actualizar_archivo(self):
        messagebox.showinfo("Guardar", "guardar actualizado")
        
    def eliminar_archivo(self):
        messagebox.showinfo("Eliminar", "eliminar actualizado")
        
    def guardar_archivo(self):
        messagebox.showinfo("Guardar", "Guardar actualizado")
        
        
    def autocompletar(self, event):
        # Obtener el texto actual del Combobox
        texto = self.nombre_combobox.get()
        
        # Filtrar las opciones que coinciden con el texto
        #if texto == '':
        if len(texto) >= 3:
            self.nombre_combobox['values'] = ("Opción 1", "Opción 2", "Opción 3")
        else:
            opciones_filtradas = [opcion for opcion in ("Opción 1", "Opción 2", "Opción 3") if texto.lower() in opcion.lower()]
            self.nombre_combobox['values'] = opciones_filtradas
        
        # Mostrar el menú desplegable
        self.nombre_combobox.event_generate('<Down>')