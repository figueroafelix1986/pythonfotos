import tkinter as tk
from tkinter import ttk, messagebox
from .common import *
from controllers.Cemployee import Employee, ControllersEmployee


class NuevoTrabajadorVentana:
    def __init__(self, root):
        self.root = root
        self.font= ("Arial", 12, "bold")
        self.nueva_ventana = tk.Toplevel(self.root)
        self.nueva_ventana.title("Datos de trabajadores")
        self.controlador=ControllersEmployee()
        self.width=25

        # Ocultar la ventana principal
        self.root.withdraw()
        # Configurar el evento de cierre de la nueva ventana
        self.nueva_ventana.protocol("WM_DELETE_WINDOW", self.on_close)

        # Crear etiquetas y campos de entrada
        # Configuración de los widgets
        tk.Label(self.nueva_ventana, text="Nombre:", font=self.font).grid(
            row=0, column=0, padx=10, pady=5, sticky="e")
        self.nombre_entry = tk.Entry(self.nueva_ventana, font=self.font, width=self.width)
        self.nombre_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        tk.Label(self.nueva_ventana, text="Apellidos:", font=self.font).grid(
            row=1, column=0, padx=10, pady=5, sticky="e")
        self.apellidos_entry = tk.Entry(self.nueva_ventana, font=self.font, width=self.width)
        self.apellidos_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        tk.Label(self.nueva_ventana, text="Salario:", font=self.font).grid(
            row=2, column=0, padx=10, pady=5, sticky="e")
        self.salario_entry = tk.Entry(self.nueva_ventana, font=self.font, width=8)
        self.salario_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        tk.Label(self.nueva_ventana, text="Correo:", font=self.font).grid(
            row=3, column=0, padx=10, pady=5, sticky="e")
        self.correo_entry = tk.Entry(self.nueva_ventana, font=self.font, width=self.width)
        self.correo_entry.grid(row=3, column=1, padx=10, pady=5, sticky="w")
        
        tk.Label(self.nueva_ventana, text="Telefono:", font=self.font).grid(
            row=4, column=0, padx=10, pady=5, sticky="e")
        self.telefono_entry = tk.Entry(self.nueva_ventana, font=self.font, width=self.width)
        self.telefono_entry.grid(row=4, column=1, padx=10, pady=5, sticky="w")
                
        tk.Label(self.nueva_ventana, text="Direccion:", font=self.font).grid(
            row=5, column=0, padx=10, pady=5, sticky="e")
        self.direccion_entry = tk.Entry(self.nueva_ventana, font=self.font, width=self.width)
        self.direccion_entry.grid(row=5, column=1, padx=10, pady=5, sticky="w")

        # Crear checkbox para activo
        self.activo_var = tk.BooleanVar(value=True)
        self.activo_checkbox = tk.Checkbutton(
            self.nueva_ventana, text="Activo", variable=self.activo_var)
        self.activo_checkbox.grid(row=6, columnspan=2, pady=5)

        # Crear un botón Guardar en la nueva ventana

        # Botón Guardar
        self.boton_guardar = tk.Button(
            self.nueva_ventana, text="Guardar", command=self.guardar_archivo, font=self.font, padx=2, pady=2,  # Color de fondo
   bg="#28A745",  # Verde brillante
    fg="white",    # Texto blanco
    borderwidth=5)
        self.boton_guardar.grid(row=1, column=2, pady=10, padx=5, sticky="ew")

        # Botón Eliminar
        self.boton_eliminar = tk.Button(
            self.nueva_ventana, text="Eliminar", command=self.eliminar_archivo, font=self.font, padx=2, pady=2,
            bg="#DC3545",  # Rojo brillante
    fg="white",    # Texto blanco
    borderwidth=5)
        self.boton_eliminar.grid(row=2, column=2, pady=10, padx=5, sticky="ew")

        # Botón Actualizar
        self.boton_actualizar = tk.Button(
            self.nueva_ventana, text="Actualizar", command=self.actualizar_archivo, font=self.font, padx=2, pady=2
            ,
    bg="#007BFF",  # Azul brillante
    fg="white",    # Texto blanco
    borderwidth=5)
        self.boton_actualizar.grid(
            row=3, column=2, pady=10, padx=5, sticky="ew")

        # Crear Treeview para listar los Fechas
        self.tree = ttk.Treeview(self.nueva_ventana, columns=(
            "ID","Nombre", "Apellidos", "Salario", "Activo", "Correo", "Telefono", "Direccion"), show='headings')
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Apellidos", text="Apellidos")
        self.tree.heading("Salario", text="Salario")        
        self.tree.heading("Activo", text="Activo")
        self.tree.heading("Correo", text="Correo")
        self.tree.heading("Telefono", text="Telefono")
        self.tree.heading("Direccion", text="Direccion")
        style = ttk.Style()
        style.configure("Treeview", font=self.font)
        self.tree.grid(row=7, columnspan=3, padx=10, pady=10)

        self.tree.column("ID", width=0, stretch=tk.NO)
        
        # Llenar el Treeview con datos existentes
        self.cargar_datos()
        self.boton_eliminar.config(state=tk.DISABLED)
        self.boton_actualizar.config(state=tk.DISABLED)
        
        self.tree.bind("<<TreeviewSelect>>", self.cargar_datos_seleccionados)

        # Centrar la ventana usando la nueva clase
        centrar = CentrarVentana(self.nueva_ventana)
        centrar.centrar()

    def cargar_datos(self):

        activos = self.controlador.listar_activos()
        datos = [(emp.id, emp.name, emp.apellidos, emp.salaries, emp.activo, emp.correo, emp.telefono, emp.direccion)
            for emp in activos]
        for dato in datos:
            self.tree.insert("", tk.END, values=dato)          
        

    def guardar_archivo(self):
        nuevo_trabajador=Employee(name = self.nombre_entry.get(),
        apellidos = self.apellidos_entry.get(),
        salaries = self.salario_entry.get(),
        correo=self.correo_entry.get(),
        activo = self.activo_var.get(),
        telefono=self.telefono_entry.get(),
        direccion = self.direccion_entry.get()
        )        
        self.controlador.guardar_employee(nuevo_trabajador)    
        # Recargar el Treeview con los datos actualizados
        self.recargar_treeview()
        self.nombre_entry.delete(0, tk.END)
        self.apellidos_entry.delete(0, tk.END)
        self.correo_entry.delete(0, tk.END)
        self.salario_entry.delete(0, tk.END)
        self.telefono_entry.delete(0, tk.END)
        self.direccion_entry.delete(0, tk.END)
        self.activo_var.set(True)
        # messagebox.showinfo("Guardar", "Archivo guardado")

    def recargar_treeview(self):
        # Limpiar el Treeview existente
        for item in self.tree.get_children():
            self.tree.delete(item)
        # Llenar el Treeview con los datos actualizados
        self.cargar_datos()

    def on_close(self):
        # Mostrar la ventana principal nuevamente
        self.root.deiconify()
        # Cerrar la ventana actual
        self.nueva_ventana.destroy()

    def cargar_datos_seleccionados(self, event):
        selected_item = self.tree.selection()[0]    
        valores = self.tree.item(selected_item, "values")

        self.nombre_entry.delete(0, tk.END)
        self.nombre_entry.insert(0, valores[1])

        self.apellidos_entry.delete(0, tk.END)
        self.apellidos_entry.insert(0, valores[2])

        self.salario_entry.delete(0, tk.END)
        self.salario_entry.insert(0, valores[3])

        self.activo_var.set(valores[4] == "True")
        
        self.correo_entry.delete(0, tk.END)
        self.correo_entry.insert(0, valores[5])
        
        self.telefono_entry.delete(0, tk.END)
        self.telefono_entry.insert(0, valores[6])
        self.direccion_entry.delete(0, tk.END)
        self.direccion_entry.insert(0, valores[7])
        
        self.boton_eliminar.config(state=tk.NORMAL)
        self.boton_actualizar.config(state=tk.NORMAL)
        self.boton_guardar.config(state=tk.DISABLED)

    def eliminar_archivo(self):        
        eliminar_trabajador=Employee(name = self.nombre_entry.get(),
        apellidos = self.apellidos_entry.get(),
        salaries = self.salario_entry.get(),
        correo = self.correo_entry.get(),
        activo = self.activo_var.get(),
        telefono=self.telefono_entry.get(),
        direccion = self.direccion_entry.get())        
        self.controlador.eliminar_employee(eliminar_trabajador) 
        
        self.recargar_treeview()
        self.nombre_entry.delete(0, tk.END)
        self.apellidos_entry.delete(0, tk.END)
        self.salario_entry.delete(0, tk.END)
        self.correo_entry.delete(0, tk.END)
        self.telefono_entry.delete(0, tk.END)
        self.direccion_entry.delete(0, tk.END)
        self.activo_var.set(False)
        self.boton_eliminar.config(state=tk.DISABLED)
        self.boton_actualizar.config(state=tk.DISABLED)
        self.boton_guardar.config(state=tk.NORMAL)
        #messagebox.showinfo("Eliminado", "Archivo eliminado")

    def actualizar_archivo(self):        
        actualizar_trabajador=Employee(name = self.nombre_entry.get(),
        apellidos = self.apellidos_entry.get(),
        salaries = self.salario_entry.get(),
        correo = self.correo_entry.get(),
        activo = self.activo_var.get(),
        telefono = self.telefono_entry.get(),
        direccion = self.direccion_entry.get())        
        self.controlador.actualizar_employee(actualizar_trabajador) 
        
        
        self.recargar_treeview()
        self.nombre_entry.delete(0, tk.END)
        self.apellidos_entry.delete(0, tk.END)
        self.salario_entry.delete(0, tk.END)
        self.correo_entry.delete(0, tk.END)
        self.telefono_entry.delete(0, tk.END)
        self.direccion_entry.delete(0, tk.END)
        self.activo_var.set(True)
        self.boton_eliminar.config(state=tk.DISABLED)
        self.boton_actualizar.config(state=tk.DISABLED)
        self.boton_guardar.config(state=tk.NORMAL)
        messagebox.showinfo("Actualizar", "Archivo actualizado")
