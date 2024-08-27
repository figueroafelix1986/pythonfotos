import tkinter as tk
from tkinter import ttk, messagebox
#from .datework import insertar_trab, list_trabj, eliminar_trab, actualizar_trab
from .common import *
from controllers.Cemployee import Employee, ControllersEmployee
from controllers.Cdate_work import DateWork, ControllersDateWork
from datetime import datetime, timedelta
from tkcalendar import DateEntry


class NuevoDatWorkVentana:
    def __init__(self, root):
        self.root = root
        self.font= ("Arial", 12)
        self.nueva_ventana = tk.Toplevel(self.root)
        self.control_datework = ControllersDateWork()
        self.nueva_ventana.title("Datos de asistencia")
        self.control_empl = ControllersEmployee()
        self.empleados_activos = self.control_empl.listar_nombre_employee()
        # self.nombres_apellidos = [nombre for nombre,salario, id in self.empleados_activos]
        self.salarios = [salario for nombre,
                         salario, id in self.empleados_activos]
        hoy = datetime.today()

        # Ocultar la ventana principal
        self.root.withdraw()
        # Configurar el evento de cierre de la nueva ventana
        self.nueva_ventana.protocol("WM_DELETE_WINDOW", self.on_close)


        # Crear etiquetas y campos de entrada
        tk.Label(self.nueva_ventana, text="Fecha", font=self.font).grid(
            row=0, column=0, padx=10, pady=5)
        self.fecha_inicio_entry = DateEntry(
            self.nueva_ventana, font=self.font, date_pattern='y-mm-dd', hoy=hoy)
        self.fecha_inicio_entry.grid(row=0, column=1, padx=10, pady=5)

        # Crear etiquetas y campos de entrada
        tk.Label(self.nueva_ventana, text="Nombre:", font=self.font).grid(
            row=1, column=0, padx=10, pady=5)
        self.nombre_combobox = ttk.Combobox(self.nueva_ventana, font=self.font)
        self.nombre_combobox['values'] = (
            [nombre for nombre,
             salario, id in self.trabajadoresPicker()])  # Añadir opciones
        self.nombre_combobox.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.nueva_ventana, text="Incidencia:", font=self.font).grid(
            row=2, column=0, padx=10, pady=5)
        self.nombre_incidencia = ttk.Combobox(
            self.nueva_ventana, font=self.font)
        self.nombre_incidencia['values'] = ('X', '-', '2')  # Añadir opciones
        self.nombre_incidencia.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self.nueva_ventana, text="Salario:", font=self.font).grid(
            row=3, column=0, padx=10, pady=5)
        self.salario_entry = tk.Entry(self.nueva_ventana, font=self.font)
        self.salario_entry.grid(row=3, column=1, padx=10, pady=5)

        # Crear Treeview para listar los Fechas
        self.tree = ttk.Treeview(self.nueva_ventana, columns=(
            "ID", "Nombre", "Fecha", "Incidencia", "Salario"), show='headings')
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Incidencia", text="Incidencia")
        self.tree.heading("Salario", text="Salario")
        style = ttk.Style()
        style.configure("Treeview", font=self.font)
        self.tree.grid(row=5, columnspan=3, padx=10, pady=10)

        self.tree.column("ID", width=0, stretch=tk.NO)

        self.id_empleado_entry = tk.Entry(self.nueva_ventana, font=self.font)
        self.id_empleado_entry.grid(row=3, column=5, padx=10, pady=5)

        # Ocultar el Entry
        self.id_empleado_entry.grid_remove()

        self.nombre_combobox.bind('<KeyRelease>', self.autocompletar)
        
        # Llenar el Treeview con datos existentes
        self.cargar_datos()






        # Crear un botón Guardar en la nueva ventana
    

        # Botón Guardar
        self.boton_guardar = tk.Button(
            self.nueva_ventana, text="Guardar", command=self.guardar_archivo, font=("Arial", 10), padx=2, pady=2)
        self.boton_guardar.grid(row=1, column=4, pady=10, padx=5, sticky="ew")

        # Botón Eliminar
        self.boton_eliminar = tk.Button(
            self.nueva_ventana, text="Eliminar", command=self.eliminar_archivo, font=("Arial", 10), padx=2, pady=2)
        self.boton_eliminar.grid(row=2, column=4, pady=10, padx=5, sticky="ew")

        # Botón Actualizar
        self.boton_actualizar = tk.Button(
            self.nueva_ventana, text="Actualizar", command=self.actualizar_archivo, font=("Arial", 10), padx=2, pady=2)
        self.boton_actualizar.grid(
            row=3, column=4, pady=10, padx=5, sticky="ew")

        self.nombre_combobox.bind(
            "<<ComboboxSelected>>", self.actualizar_salario)
        
        self.fecha_inicio_entry.bind(
            "<<DateEntrySelected>>", self.on_date_selected)

        centrar = CentrarVentana(self.nueva_ventana)
        centrar.centrar()

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
        datos_datework = DateWork(date=self.fecha_inicio_entry.get_date(),
                                  work=self.nombre_incidencia.get(),
                                  salaries=self.salario_entry.get(),
                                  employee_id=self.id_empleado_entry.get())
        self.control_datework.guardar_date_work(datos_datework)
        self.recargar_treeview()

        # Actualizar la lista de empleados y el Combobox
        #self.actualizar_lista_empleados()
        #self.nombre_combobox['values'] = self.nombres_apellidos

        # messagebox.showinfo("Guardar", "Guardar actualizado")
        # self.fecha_inicio_entry.delete(0, tk.END)
        #self.nombre_combobox.delete(0, tk.END)
        # self.nombre_incidencia.delete(0, tk.END)
        self.salario_entry.delete(0, tk.END)
        self.id_empleado_entry.delete(0, tk.END)

    def on_date_selected(self, event):
        # self.nombre_combobox.delete(0, tk.END)
        self.nombre_incidencia.delete(0, tk.END)
        self.salario_entry.delete(0, tk.END)
        self.recargar_treeview()

    def recargar_treeview(self):
        # Limpiar el Treeview existente
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Llenar el Treeview con los datos actualizados
        self.cargar_datos()
        
        self.nombre_combobox.delete(0, tk.END)
        
        # Actualizar la lista de empleados y el Combobox
        # self.actualizar_lista_empleados()
        self.nombre_combobox['values'] = (
            [nombre for nombre,
             salario, id in self.trabajadoresPicker()])
        
    def autocompletar(self, event):
        # Obtener el texto actual del Combobox
        texto = self.nombre_combobox.get()
        
        while len(texto) < 3:
            return

        self.actualizar_lista_empleados()


        # Filtrar las opciones que coinciden con el texto
        opciones_filtradas = [opcion for opcion in (
            self.nombres_apellidos) if texto.lower() in opcion.lower()]
        self.nombre_combobox['values'] = opciones_filtradas
        
        # Mantener el texto actual del Combobox
        self.nombre_combobox.set(texto)

        # Mostrar el menú desplegable
        self.nombre_combobox.event_generate('<Down>')

    def cargar_datos(self):

        activos = self.control_datework.listar_date_work(
            self.fecha_inicio_entry.get_date())
        # self.control_empl.get_trabajador_id()
        datos = [(emp.id, self.control_empl.get_trabajador_id(emp.employee_id), emp.date, emp.work, emp.salaries)
                 for emp in activos]
        for dato in datos:
            self.tree.insert("", tk.END, values=dato)

    def actualizar_salario(self, event):
        # Obtener el nombre seleccionado
        nombre_seleccionado = self.nombre_combobox.get()

        # Buscar el salario correspondiente
        for nombre, salario, id in self.empleados_activos:
            if nombre == nombre_seleccionado:
                self.salario_entry.delete(0, tk.END)
                self.salario_entry.insert(0, str(salario))
                self.id_empleado_entry.delete(0, tk.END)
                self.id_empleado_entry.insert(0, str(id))
                break

    def trabajadoresPicker(self):
        activos = self.control_datework.listar_date_work(
            self.fecha_inicio_entry.get_date())
        listId = []
        listTrab = []
        for x in activos:
            listId.append(x.employee_id)

        for trab in self.empleados_activos:
            if trab[2] not in listId:
                listTrab.append(trab)

        return listTrab

    def actualizar_lista_empleados(self):
        self.empleados_activos = self.trabajadoresPicker()
        self.nombres_apellidos = [nombre for nombre,
                                  salario, id in self.empleados_activos]
        self.salarios = [salario for nombre,
                         salario, id in self.empleados_activos]
