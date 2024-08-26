from create_dabase import db
from modelos.Mdate_activ import DateActive
from tkinter import messagebox
from sqlalchemy import desc

session = db.get_session()


class ControllersDateActive:
    def __init__(self):
        pass  # Puedes inicializar variables o configuraciones aquí si es necesario
        self.prueba=self.actualizar_false(self)

    def guardar_date_active(self, objeto):
        
        try:
            # Convertir las fechas a cadenas para la comparación
            date_ini_str = objeto.date_ini.strftime('%Y-%m-%d')
            date_fin_str = objeto.dete_fin.strftime('%Y-%m-%d')
            
            # Verificar si el objeto ya existe
            existing_obj = session.query(DateActive).filter_by(date_ini=date_ini_str,
                                                               dete_fin=date_fin_str).first()

            if existing_obj:
                messagebox.showerror(
                    "Guardar", "La fecha ya existe en la base de datos.")

                # print("El empleado ya existe en la base de datos.")
            else: 
                self.prueba              
                session.add(objeto)
                session.commit()
                
                messagebox.showinfo("Guardar", "Se guardo con exito")
        except Exception as e:
            session.rollback()
            print(f"Error al guardar el objeto: {e}")

    def actualizar_date_active(self, objeto):
        existing_obj = session.query(DateActive).filter_by(
            date_ini=objeto.date_ini,
            dete_fin=objeto.dete_fin

        ).first()
        if existing_obj:
            existing_obj.activo = objeto.activo
            session.commit()

    def listar_date_active(self):
        try:
            activos = session.query(DateActive).filter_by(activo=True).order_by(desc(DateActive.date_ini)).all()
            return activos
        except Exception as e:
            print(f"Error al listar fechas activos: {e}")
            return []

    def actualizar_false(self, objeto):            
            session.query(DateActive).update({DateActive.activo: False})
            session.commit()