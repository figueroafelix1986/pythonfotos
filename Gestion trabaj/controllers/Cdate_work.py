from create_dabase import db
from modelos.Mdate_work import DateWork
from tkinter import messagebox


session = db.get_session()


class ControllersDateWork:
    def __init__(self):
        pass  # Puedes inicializar variables o configuraciones aquí si es necesario

    def guardar_date_work(self, objeto):
        try:
            salaries_num = float(objeto.salaries)  # Usa float() si los salarios pueden ser decimales, si no usa int()
            
            # Multiplicar el salario si work es '2'
            if objeto.work == '2':
                objeto.salaries = salaries_num * 2
            else:
                objeto.salaries
            
            # Verificar si el objeto ya existe
            existing_obj = session.query(DateWork).filter_by(date=objeto.date,
                                                            work=objeto.work,
                                                            salaries=objeto.salaries,
                                                            employee_id=objeto.employee_id).first()

            if existing_obj:
                messagebox.showerror("Guardar", "El día ya existe en la base de datos.")
            else:                
                session.add(objeto)
                session.commit()
                messagebox.showinfo("Guardar", "Se guardó con éxito")
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
        salaries_num = float(objeto.salaries)  # Usa float() si los salarios pueden ser decimales, si no usa int()
            
        salaries_num = float(objeto.salaries)  # Usa float() si los salarios pueden ser decimales, si no usa int()
            
            # Multiplicar el salario si work es '2'
        if objeto.work == '2':
            objeto.salaries = salaries_num * 2
        else:
            objeto.salaries
        
        datework = session.query(DateWork).filter_by(
            date=objeto.date,
            employee_id=objeto.employee_id
        ).first()
        if datework:
            datework.salaries=objeto.salaries
            datework.work=objeto.work
            session.commit()
            
            
    def listar_date_work(self,date):
        try:
            list_datework = session.query(DateWork).filter_by(date=date).all()           
            return list_datework
        except Exception as e:
            print(f"Error al listar dias trabajados activos: {e}")
            return []
        
    def listar_date_work_range(self, start_date, end_date):
        try:
            list_datework = session.query(DateWork).filter(DateWork.date.between(start_date, end_date)).all()
            return list_datework
        except Exception as e:
            print(f"Error al listar días trabajados en el rango de fechas: {e}")
            return []
