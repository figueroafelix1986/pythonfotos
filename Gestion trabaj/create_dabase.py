
from modelos.database import Database
from modelos.librery import Base
from modelos.Mdate_work import DateWork
from modelos.Memployee import Employee
from modelos.Mdate_activ import DateActive
from modelos.Mcuentas import Cuentas
from modelos.Msubcuenta import SubCuentas
from modelos.Mcuenta_subcuenta import CuentaSubCuenta



# Crear la base de datos con todas las bases
db = Database('sqlite:///gestion_empleados.db', Base)
