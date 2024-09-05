from modelos.librery import Base, Column, Integer, String, DECIMAL, BOOLEAN, DATE, ForeignKey,relationship

class CuentaSubCuenta(Base):
    __tablename__ = 'cuenta_subcuenta'
    id = Column(Integer, primary_key=True)
    cuenta_id = Column(Integer, ForeignKey('cuentas.id'))
    subcuenta_id = Column(Integer, ForeignKey('subcuentas.id'))
    monto = Column(DECIMAL)
    fecha = Column(DATE)
    tipocuenta=Column(String)

    cuenta = relationship("Cuentas", back_populates="subcuentas")
    subcuenta = relationship("SubCuentas", back_populates="cuentas")
