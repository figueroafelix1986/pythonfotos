from create_dabase import db
from modelos.Mdate_work import DateWork
from tkinter import messagebox


session = db.get_session()


class ControllersDateWork:
    def __init__(self):
        pass  # Puedes inicializar variables o configuraciones aquí si es necesario

    def guardar_date_work(self, objeto):
        try:
            # Verificar si el objeto ya existe
            existing_obj = session.query(DateWork).filter_by(date=objeto.date,
                                                             work=objeto.apellidos,
                                                             salaries=objeto.salaries,
                                                             employe_id=objeto.activo).first()

            if existing_obj:
                messagebox.showerror(
                    "Guardar", "El dia ya existe en la base de datos.")

                # print("El empleado ya existe en la base de datos.")
            else:
                session.add(objeto)
                session.commit()
                messagebox.showinfo("Guardar", "Se guardo con exito")
        except Exception as e:
            session.rollback()
            print(f"Error al guardar el objeto: {e}")

    def eliminar_date_work(self, objeto):
        datework = session.query(DateWork).filter_by(
            date=objeto.date,
            work=objeto.apellidos,
            salaries=objeto.salaries,
            employe_id=objeto.activo
        ).first()
        if datework:
            session.delete(datework)
            session.commit()
            
            
    def actualizar_date_work(self, objeto):
        datework = session.query(DateWork).filter_by(
            date=objeto.date,
            work=objeto.apellidos
        ).first()
        if datework:
            datework.salaries=objeto.salaries,
            datework.employe_id=objeto.activo
            session.commit()
            
            
    def listar_activos(self):
        try:
            activos = session.query(DateWork).filter_by(activo=True).all()
            return activos
        except Exception as e:
            print(f"Error al listar dias trabajados activos: {e}")
            return []