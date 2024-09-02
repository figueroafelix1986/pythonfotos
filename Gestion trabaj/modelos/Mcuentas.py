from modelos.librery import Base, Column, Integer, String, DECIMAL, BOOLEAN, relationship


class Cuentas(Base):
    __tablename__ = 'cuentas'
    id = Column(Integer, primary_key=True)
    code = Column(String)
    nombre = Column(String)
    activo = Column(BOOLEAN)
    
    #subcuentas = relationship('Subcuenta', back_populates='cuentas')

    def __init__(self, code, nombre, activo):
        self.code = code
        self.nombre = nombre
        self.activo = activo
