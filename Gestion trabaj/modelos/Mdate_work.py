from datetime import datetime
from modelos.librery import Base, Column, Integer, DateTime, VARCHAR, ForeignKey, DECIMAL


class DateWork(Base):
    __tablename__ = 'date_work'
    id = Column(Integer, primary_key=True)
    date = Column(DateTime)
    work = Column(VARCHAR)
    salaries = Column(DECIMAL)
    employee_id = Column(Integer, ForeignKey('empleados.id'))

    def __init__(self, date, work, salaries, employee_id):
        self.date = date
        self.work = work
        self.salaries = salaries
        self.employee_id = employee_id
