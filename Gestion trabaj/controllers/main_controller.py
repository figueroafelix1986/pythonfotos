from modelos.database import Database
from modelos.Memployee import *

db=Database()

session = db.get_session()


class Controllers():
    # def __init__(self):

    def save(self, objeto):
        session.add(objeto)
        session.commit()


# Ejemplo de agregar un empleado
new_employee = Employee(
    name='John Doe', apellidos='Developer', activo=True, salaries=54)

Controllers.save(new_employee)

# session.add(new_employee)
# session.commit()

# new_datework = DateWork(date=datetime.now(), work=True, employee_id=1)
# session.add(new_datework)

# session.commit()
