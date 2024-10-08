from modelos.librery import Base, Column, Integer, String, DECIMAL, BOOLEAN, relationship


class Employee(Base):
    __tablename__ = 'empleados'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    apellidos = Column(String)
    correo=Column(String)
    salaries = Column(DECIMAL(precision=10, scale=2))
    activo = Column(BOOLEAN)
    date_works = relationship('DateWork', backref='employee',
                              cascade="all, delete-orphan", passive_deletes=True)
    telefono=Column(String)
    direccion=Column(String)
    # salaries = relationship('DateWork', backref='employee')

    def __init__(self, name, apellidos, salaries, activo,correo,telefono,direccion):
        self.name = name
        self.apellidos = apellidos
        self.salaries = salaries
        self.correo=correo
        self.activo = activo
        self.telefono=telefono
        self.direccion=direccion
