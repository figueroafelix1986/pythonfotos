from datetime import datetime
from modelos.librery import Base, Column, Integer, DateTime, VARCHAR, ForeignKey, DECIMAL,BOOLEAN,DATE
from sqlalchemy.sql import func


class DateActive(Base):
    __tablename__ = 'date_active'
    id = Column(Integer, primary_key=True)
    date_ini = Column(DATE)
    dete_fin = Column(DATE)
    activo = Column(BOOLEAN)
    date_created = Column(DateTime, default=func.now()) 

    def __init__(self, date_ini, dete_fin, activo, date_created=None):
        self.date_ini = date_ini
        self.dete_fin = dete_fin
        self.activo = activo
        if date_created is None:
            self.date_created = func.now()
        else:
            self.date_created = date_created