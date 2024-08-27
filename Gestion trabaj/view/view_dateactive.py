import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from datetime import datetime, timedelta
from .common import *
from controllers.Cdate_active import DateActive, ControllersDateActive

# dateactive_class = ControllersDateActive()


class NuevodateActive:
    def __init__(self, root):
        self.root = root
        self.font = ("Arial", 12)
        self.nueva_ventana = tk.Toplevel(self.root)
        self.nueva_ventana.title("Fecha Activa")
        self.padx = 10
        self.pady = 5
        self.controler = ControllersDateActive()

        hoy = datetime.today()
        primer_dia_mes = hoy.replace(day=1)
        ultimo_dia_mes = (primer_dia_mes + timedelta(days=32)
                          ).replace(day=1) - timedelta(days=1)

        # Ocultar la ventana principal
        self.root.withdraw()
        # Configurar el evento de cierre de la nueva ventana
        self.nueva_ventana.protocol("WM_DELETE_WINDOW", self.on_close)

        # Crear etiquetas y campos de entrada
        tk.Label(self.nueva_ventana, text="Fecha Inicio:", font=self.font).grid(
            row=0, column=0, padx=self.padx, pady=self.pady)
        self.fecha_inicio_entry = DateEntry(self.nueva_ventana, font=self.font, date_pattern='y-mm-dd',
                                            year=primer_dia_mes.year, month=primer_dia_mes.month, day=primer_dia_mes.day)
        self.fecha_inicio_entry.grid(
            row=0, column=1, padx=self.padx, pady=self.pady)

        ultimo_dia_mes = (self.fecha_inicio_entry.get_date() + timedelta(days=32)
                          ).replace(day=1) - timedelta(days=1)

        tk.Label(self.nueva_ventana, text="Fecha Fin:", font=self.font).grid(
            row=0, column=2, padx=self.padx, pady=self.pady)
        self.fecha_fin_entry = DateEntry(self.nueva_ventana, font=self.font, date_pattern='y-mm-dd',
                                         year=ultimo_dia_mes.year, month=ultimo_dia_mes.month, day=ultimo_dia_mes.day)
        self.fecha_fin_entry.grid(
            row=0, column=3, padx=self.padx, pady=self.pady)
        
        self.fecha_fin_entry.config(state='disabled')

        # Crear checkbox para activo
        self.activo_var = tk.BooleanVar(value=True)
        self.activo_checkbox = tk.Checkbutton(
            self.nueva_ventana, text="Activo", variable=self.activo_var)
        self.activo_checkbox.grid(row=3, columnspan=2, pady=5)

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
            "Fecha_Inicio", "Fecha_Fin",  "Activo"), show='headings')
        self.tree.heading("Fecha_Inicio", text="Fecha Inicio")
        self.tree.heading("Fecha_Fin", text="Fecha Fin")
        self.tree.heading("Activo", text="Activo")
        style = ttk.Style()
        style.configure("Treeview", font=self.font)
        self.tree.grid(row=5, columnspan=5, padx=10, pady=10)

        self.tree.bind("<<TreeviewSelect>>", self.cargar_datos_seleccionados)
        self.fecha_inicio_entry.bind(
            "<<DateEntrySelected>>", self.actualizar_fecha_fin)

        # Centrar la ventana usando la nueva clase
        centrar = CentrarVentana(self.nueva_ventana)
        centrar.centrar()

        # Llenar el Treeview con datos existentes
        self.cargar_datos()
        self.boton_eliminar.config(state=tk.DISABLED)
        self.boton_actualizar.config(state=tk.DISABLED)
        


    def cargar_datos(self):

        activos = self.controler.listar_date_active()
        datos = [(emp.date_ini, emp.dete_fin, emp.activo)
                 for emp in activos]
        for dato in datos:
            self.tree.insert("", tk.END, values=dato)


    def guardar_archivo(self):

        date_activo = DateActive(date_ini=self.fecha_inicio_entry.get_date(),
                                 dete_fin=self.fecha_fin_entry.get_date(),
                                 activo=self.activo_var.get())
        self.controler.guardar_date_active(date_activo)
        # messagebox.showinfo("Guardar")
        self.recargar_treeview()
        # self.fecha_inicio_entry.delete(0, tk.END)
        # self.fecha_fin_entry.delete(0, tk.END)
        self.activo_var.set(True)

    def eliminar_archivo(self):
        messagebox.showinfo("Eliminar")

    def actualizar_archivo(self):
        messagebox.showinfo("Actualizar")

    def on_close(self):
        # Mostrar la ventana principal nuevamente
        self.root.deiconify()
        # Cerrar la ventana actual
        self.nueva_ventana.destroy()

    def recargar_treeview(self):
        # Limpiar el Treeview existente
        for item in self.tree.get_children():
            self.tree.delete(item)
        # Llenar el Treeview con los datos actualizados
        self.cargar_datos()

    def cargar_datos_seleccionados(self, event):
        selected_item = self.tree.selection()[0]
        valores = self.tree.item(selected_item, "values")

        # Cargar los valores en los campos de entrada
        self.fecha_inicio_entry.delete(0, tk.END)
        self.fecha_inicio_entry.insert(0, valores[0])

        self.fecha_fin_entry.config(state='enabled')

        self.fecha_fin_entry.delete(0, tk.END)
        self.fecha_fin_entry.insert(0, valores[1])
        self.fecha_fin_entry.config(state='disabled')

        self.activo_var.set(valores[2] == "True")
        self.boton_eliminar.config(state=tk.NORMAL)
        self.boton_actualizar.config(state=tk.NORMAL)
        self.boton_guardar.config(state=tk.DISABLED)
        
    def actualizar_fecha_fin(self, event):
        print("Prueba")
        # Obtener la nueva fecha de inicio
        nueva_fecha_ini = self.fecha_inicio_entry.get_date()
        # Calcular el último día del mes basado en la nueva fecha de inicio
        ultimo_dia_mes = (nueva_fecha_ini + timedelta(days=32)).replace(day=1) - timedelta(days=1)
        # Actualizar la fecha de fin
        # self.fecha_fin_entry.set_date(ultimo_dia_mes)
        self.fecha_fin_entry = DateEntry(self.nueva_ventana, font=self.font, date_pattern='y-mm-dd',
                                         year=ultimo_dia_mes.year, month=ultimo_dia_mes.month, day=ultimo_dia_mes.day)
        self.fecha_fin_entry.grid(
            row=0, column=3, padx=self.padx, pady=self.pady)
        self.fecha_fin_entry.config(state='disabled')
