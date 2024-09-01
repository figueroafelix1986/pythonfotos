from modelos.librery import Base, Column, Integer, String, DECIMAL, BOOLEAN, relationship,ForeignKey,Table


cuentas_subcuentas = Table('cuentas_subcuentas', Base.metadata,
    Column('cuenta_id', Integer, ForeignKey('cuentas.id'), primary_key=True),
    Column('subcuenta_id', Integer, ForeignKey('sub_cuentas.id'), primary_key=True)
)