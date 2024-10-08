from create_dabase import db
from modelos.Memployee import Employee
from modelos.Mdate_work import DateWork
from tkinter import messagebox

session = db.get_session()


class ControllersEmployee:
    def __init__(self):
        pass  # Puedes inicializar variables o configuraciones aquí si es necesario

    def guardar_employee(self, objeto):
        try:
            objeto.name = objeto.name.title()
            objeto.apellidos = objeto.apellidos.title()
            
            # Verificar si el objeto ya existe
            existing_obj = session.query(Employee).filter_by(name=objeto.name,
                                                             apellidos=objeto.apellidos
                                                             ).first()

            if existing_obj:
                messagebox.showerror(
                    "Guardar", "El empleado ya existe en la base de datos.")

                # print("El empleado ya existe en la base de datos.")
            else:
                session.add(objeto)
                session.commit()
                messagebox.showinfo("Guardar", "Se guardo con exito")
        except Exception as e:
            session.rollback()
            messagebox.showerror("ERROR",f"Error al guardar el objeto: {e}")

    def eliminar_employee(self, objeto):
        employee = session.query(Employee).filter_by(
        name=objeto.name,
        apellidos=objeto.apellidos,
        salaries=objeto.salaries,
        correo=objeto.correo,
        telefono=objeto.telefono,
        direccion=objeto.direccion,
        activo=objeto.activo
    ).first()
    
        if employee:
            if session.query(DateWork).filter_by(employee_id=employee.id).count() > 0:
                messagebox.showerror("Eliminar", "No se puede eliminar el empleado porque tiene registros asociados.")
            else:
                try:
                    session.delete(employee)
                    session.commit()
                    messagebox.showinfo("Eliminar", "Empleado eliminado exitosamente.")
                except:
                    session.rollback()
                    messagebox.showerror("Eliminar", "Error al eliminar el empleado")
        else:
            messagebox.showerror("Eliminar", "Empleado no encontrado.")
            

    def actualizar_employee(self, objeto):
        employee = session.query(Employee).filter_by(
            name=objeto.name,
            apellidos=objeto.apellidos
        ).first()
        if employee:
            employee.correo=objeto.correo
            employee.salaries = objeto.salaries
            employee.activo = objeto.activo
            employee.telefono=objeto.telefono
            employee.direccion=objeto.direccion
            session.commit()

    def listar_activos(self):
        try:
            #activos = session.query(Employee).filter_by(activo=True).all()
            activos = session.query(Employee).all()
            return activos
        except Exception as e:
            print(f"Error al listar empleados activos: {e}")
            return []
        
        
    def listar_nombre_employee(self):
        try:
            activos = session.query(Employee).filter_by(activo=True).all()
            return [(f"{empleado.name} {empleado.apellidos} ",empleado.salaries,empleado.id) for empleado in activos]
        except Exception as e:
            print(f"Error al listar empleados activos: {e}")
            return []
        
        
    def get_trabajador_id(self, id_trabajador):
        try:
            activo = session.query(Employee).filter_by(id=id_trabajador).first()
            if activo:
                return f"{activo.name} {activo.apellidos}"
            else:
                return "Desconocido"
        except Exception as e:
            print(f"Error al obtener el nombre del trabajador: {e}")
            return "Error"
