import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from datetime import datetime, timedelta
from .common import *
from controllers.Csubcuenta import SubCuentas, ControllerSubCuentas


class NuevaSubCuenta:
    def __init__(self, root):
        self.root = root
        self.font = ("Arial", 12)
        self.nueva_ventana = tk.Toplevel(self.root)
        self.nueva_ventana.title("Agergar SubCuenta")
        self.padx = 10
        self.pady = 5
        self.controler = ControllerSubCuentas()

    # Ocultar la ventana principal
        self.root.withdraw()
        # Configurar el evento de cierre de la nueva ventana
        self.nueva_ventana.protocol("WM_DELETE_WINDOW", self.on_close)


        tk.Label(self.nueva_ventana, text="Codigo:", font=self.font).grid(
            row=0, column=0, padx=10, pady=5, sticky="e")
        self.codigo_entry = tk.Entry(
            self.nueva_ventana, font=self.font, width=8)
        self.codigo_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        tk.Label(self.nueva_ventana, text="Cuenta:", font=self.font).grid(
            row=1, column=0, padx=10, pady=5, sticky="e")
        self.cuenta_entry = tk.Entry(
            self.nueva_ventana, font=self.font, width=30)
        self.cuenta_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        # Crear checkbox para activo
        self.activo_var = tk.BooleanVar(value=True)
        self.activo_checkbox = tk.Checkbutton(
            self.nueva_ventana, text="Activo", variable=self.activo_var)
        self.activo_checkbox.grid(row=2, columnspan=2, pady=5)

        # Botón Guardar
        self.boton_guardar = tk.Button(
            self.nueva_ventana, text="Guardar", command=self.guardar_archivo, font=self.font, padx=2, pady=2)
        self.boton_guardar.grid(
            row=1, column=4, padx=self.padx, pady=self.pady, sticky="ew")

        # Botón Eliminar
        self.boton_eliminar = tk.Button(
            self.nueva_ventana, text="Eliminar", command=self.eliminar_archivo, font=self.font, padx=2, pady=2)
        self.boton_eliminar.grid(
            row=2, column=4, padx=self.padx, pady=self.pady, sticky="ew")

        # Botón Actualizar
        self.boton_actualizar = tk.Button(
            self.nueva_ventana, text="Actualizar", command=self.actualizar_archivo, font=self.font, padx=2, pady=2)
        self.boton_actualizar.grid(
            row=3, column=4, pady=10, padx=5, sticky="ew")

        # Crear Treeview para listar los empleados
        self.tree = ttk.Treeview(self.nueva_ventana, columns=(
            "Codigo", "Cuenta",  "Activo"), show='headings')
        self.tree.heading("Codigo", text="Codigo")
        self.tree.heading("Cuenta", text="Nombre Cuenta")
        self.tree.heading("Activo", text="Activo")
        style = ttk.Style()
        style.configure("Treeview", font=self.font)
        self.tree.grid(row=5, columnspan=5, padx=10, pady=10)

        # self.tree.bind("<<TreeviewSelect>>", self.cargar_datos_seleccionados)
        # self.fecha_inicio_entry.bind("<<DateEntrySelected>>", self.actualizar_fecha_fin)

        # Centrar la ventana usando la nueva clase
        centrar = CentrarVentana(self.nueva_ventana)
        centrar.centrar()

        # Llenar el Treeview con datos existentes
        # self.cargar_datos()
        self.boton_eliminar.config(state=tk.DISABLED)
        self.boton_actualizar.config(state=tk.DISABLED)

    def on_close(self):
        # Mostrar la ventana principal nuevamente
        self.root.deiconify()
        # Cerrar la ventana actual
        self.nueva_ventana.destroy()

    def guardar_archivo(self):
        nuevo_cuenta=SubCuentas(code = self.codigo_entry.get(),
        nombre = self.cuenta_entry.get(),    
        activo = self.activo_var.get()
        )        
        self.controler.guardar_subcuenta(nuevo_cuenta)    
        # Recargar el Treeview con los datos actualizados
        #self.recargar_treeview()
        self.codigo_entry.delete(0, tk.END)
        self.cuenta_entry.delete(0, tk.END)       
        self.activo_var.set(True)
        #messagebox.showinfo("Guardar", "Guardar info")

    def eliminar_archivo(self):
        messagebox.showinfo("Eliminar", "Guardar info")

    def actualizar_archivo(self):
        messagebox.showinfo("Actualizar", "Guardar info")
