from modelos.librery import Base, Column, Integer, String, DECIMAL, BOOLEAN, relationship


class SubCuentas(Base):
    __tablename__ = 'subcuentas'
    id = Column(Integer, primary_key=True)
    code = Column(String)
    nombre = Column(String)
    activo = Column(BOOLEAN)
    
    cuentas = relationship("CuentaSubCuenta", back_populates="subcuenta")


    def __init__(self, code, nombre, activo):
        self.code = code
        self.nombre = nombre
        self.activo = activo
