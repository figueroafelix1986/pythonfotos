from create_dabase import db
from modelos.Msubcuenta import SubCuentas
from tkinter import messagebox
from sqlalchemy import desc

session = db.get_session()


class ControllerSubCuentas:
    def __init__(self):
        pass  # Puedes inicializar variables o configuraciones aquí si es necesario

    def guardar_subcuenta(self, objeto):
        try:
            # Verificar si el objeto ya existe
            existing_obj = session.query(SubCuentas).filter_by(code=objeto.code,
                                                               nombre=objeto.nombre,
                                                               activo=objeto.activo
                                                               ).first()

            if existing_obj:
                messagebox.showerror(
                    "Guardar", "La cuenta ya existe en la base de datos.")

                # print("El empleado ya existe en la base de datos.")
            else:
                session.add(objeto)
                session.commit()
                messagebox.showinfo("Guardar", "Se guardo con exito")
        except Exception as e:
            session.rollback()
            messagebox.showerror("ERROR", f"Error al guardar el objeto: {e}")

    def eliminar_subcuenta(self, objeto):
        deletecuenta = session.query(SubCuentas).filter_by(
            code=objeto.code,
            nombre=objeto.nombre,
            activo=objeto.activo
        ).first()
        if deletecuenta:
            session.delete(deletecuenta)
            session.commit()

    def listar_subcuentas(self):
        try:
            list_cuentas = session.query(SubCuentas).all()          
            return list_cuentas
        except Exception as e:
            print(f"Error al listar dias trabajados activos: {e}")
            return []