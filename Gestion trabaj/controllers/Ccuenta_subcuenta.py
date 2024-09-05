from create_dabase import db
from modelos.Mcuenta_subcuenta import CuentaSubCuenta
from tkinter import messagebox
from sqlalchemy import desc


session = db.get_session()


class ControllerCuentaSubCuentas:
    def __init__(self):
        pass  # Puedes inicializar variables o configuraciones aquí si es necesario

    def guardar_cuenta_subcuenta(self, objeto):
        try:
            # Verificar si el objeto ya existe
            existing_obj = session.query(CuentaSubCuenta).filter_by(cuenta_id=objeto.cuenta_id,
                                                               subcuenta_id=objeto.subcuenta_id,
                                                               monto=objeto.monto,
                                                               fecha=objeto.fecha,
                                                               tipocuenta=objeto.tipocuenta
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