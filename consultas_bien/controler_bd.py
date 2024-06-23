from librerias import *


class ConsultaPostgreSQL:
    def __init__(self, conexion):
        self.conexion = conexion

    def ejecutar_consulta(self, consulta):
        resultado = None
        try:
            with self.conexion.cursor() as cursor:
                cursor.execute(consulta)
                resultado = cursor.fetchall()
        except Exception as e:
            print(f"Ocurrió un error al ejecutar la consulta: {e}")
        
        return resultado
    
    
    def eliminar(self, consulta):
        try:
            with self.conexion.cursor() as cursor:
                cursor.execute(consulta)
                self.conexion.commit() 
                print("Datos eliminados correctamente.")
        except Exception as e:
            print(f"Ocurrió un error al eliminar los datos: {e}")
            self.conexion.rollback()  # En caso de error, deshacer los cambios
    
            
    def insertar(self, consulta):
        try:
            with self.conexion.cursor() as cursor:
                cursor.execute(consulta)
                self.conexion.commit()
                print("Datos insertados correctamente.")
        except Exception as e:
            print(f"Ocurrió un error al insertar los datos: {e}")
            self.conexion.rollback()  # En caso de error, deshacer los cambios

    def cerrar_conexion(self):
        if self.conexion:
            self.conexion.close()
            print("Conexión cerrada correctamente.")
        