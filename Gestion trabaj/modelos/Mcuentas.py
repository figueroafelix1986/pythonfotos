from modelos.librery import Base, Column, Integer, String, DECIMAL, BOOLEAN, relationship
from .cuentas_subcuentas import cuentas_subcuentas


class Cuentas(Base):
    __tablename__ = 'cuentas'
    id = Column(Integer, primary_key=True)
    code = Column(String)
    nombre = Column(String)    
    
    subcuentas = relationship('Subcuenta', secondary=cuentas_subcuentas, back_populates='cuentas')

    def __init__(self, code, nombre):
        self.code = code
        self.nombre = nombre
        