from conexion_bd import *
from controler_bd import *
from datos_usuario import *


datos_usuario=Datos_usuario()
nomb_usuario=datos_usuario.usuario()
nombre_pc=datos_usuario.nombre_pc()

# Crear una instancia de la clase ConexionPostgreSQL
conexion_db = ConexionDB('datos_encriptados')
conexion_db.cargar_conexiones()
# Crear una instancia de la clase ConsultaPostgreSQL
consulta_db = ConsultaPostgreSQL(conexion_db.conexion_pg())

# Ejemplo de uso de la clase ConsultaPostgreSQL para ejecutar una consulta
resultado = consulta_db.ejecutar_consulta("SELECT * FROM personal")
#eliminar
consulta_db.eliminar("DELETE FROM est_eval_mn")
consulta_db.insertar("""INSERT INTO est_eval_mn (id,id_person,dato_1,dato_2,dato_3,dato_4,evaluacion,imp_1,imp_2,imp_3,imp_4,incluido,fk_1,fk_2)
Select  row_number() over (), id_person,dato_1,dato_2,dato_3,dato_4,evaluacion,imp_1,imp_2,imp_3,imp_4,incluido,cgrupo_estim_mn_fk,cgrupo_afect_mn_fk  From est_mn 
WHERE est_mn.id>0;""")
consulta_db.cerrar_conexion()
print(resultado)
print(nomb_usuario)
print(nombre_pc)