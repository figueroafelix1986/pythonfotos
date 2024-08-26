from create_dabase import db
from modelos.Memployee import Employee
from tkinter import messagebox

session = db.get_session()


class ControllersEmployee:
    def __init__(self):
        pass  # Puedes inicializar variables o configuraciones aquí si es necesario

    def guardar_employee(self, objeto):
        try:
            # Verificar si el objeto ya existe
            existing_obj = session.query(Employee).filter_by(name=objeto.name,
                                                             apellidos=objeto.apellidos,
                                                             salaries=objeto.salaries,
                                                             activo=objeto.activo).first()

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
            print(f"Error al guardar el objeto: {e}")

    def eliminar_employee(self, objeto):
        employee = session.query(Employee).filter_by(
            name=objeto.name,
            apellidos=objeto.apellidos,
            salaries=objeto.salaries,
            activo=objeto.activo
        ).first()
        if employee:
            session.delete(employee)
            session.commit()

    def actualizar_employee(self, objeto):
        employee = session.query(Employee).filter_by(
            name=objeto.name,
            apellidos=objeto.apellidos
        ).first()
        if employee:
            employee.salaries = objeto.salaries
            employee.activo = objeto.activo
            session.commit()

    def listar_activos(self):
        try:
            activos = session.query(Employee).filter_by(activo=True).all()
            return activos
        except Exception as e:
            print(f"Error al listar empleados activos: {e}")
            return []
