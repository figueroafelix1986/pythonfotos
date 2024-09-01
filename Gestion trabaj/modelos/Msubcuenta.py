from modelos.librery import Base, Column, Integer, String, DECIMAL, BOOLEAN, relationship
from .cuentas_subcuentas import cuentas_subcuentas


class Subcuenta(Base):
    __tablename__ = 'sub_cuentas'
    id = Column(Integer, primary_key=True)
    code = Column(String)
    nombre = Column(String)    
    
    cuentas = relationship('Cuentas', secondary=cuentas_subcuentas, back_populates='subcuentas')

    def __init__(self, code, nombre):
        self.code = code
        self.nombre = nombre
        