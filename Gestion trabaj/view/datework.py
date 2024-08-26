from controllers.Cdate_work import DateWork, ControllersDateWork
from modelos.librery import datetime


datework_class = ControllersDateWork()

new_datework = DateWork(date=datetime.now(), work=True, salaries=56, employee_id=1)
prueba = ControllersDateWork()
prueba.guardar_date_work(new_datework)