from create_dabase import db
from modelos.Mcuentas import Cuentas
#from modelos.Msubcuenta import Subcuenta
#from modelos.cuentas_subcuentas import CuentasSubcuentas
from tkinter import messagebox
from sqlalchemy import desc

session = db.get_session()


class CcuentaSubcuenta:
    def __init__(self):
        pass  # Puedes inicializar variables o configuraciones aquí si es necesario

    def guardar_cuenta(self, objeto):
        try:
            # Verificar si el objeto ya existe
            existing_obj = session.query(Cuentas).filter_by(code=objeto.code,
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
