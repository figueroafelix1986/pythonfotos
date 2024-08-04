from librerias import *

class ConexionDB:
    def __init__(self, file_path):
        self.file_path = file_path
        self.conexiones = {}

    def cargar_conexiones(self):
        # Cargamos la clave desde el archivo .key
        clave = open("datos_", "rb").read()
        # Creamos el objeto Fernet con la clave
        fernet = Fernet(clave)
        # Abrimos el fichero encriptado
        with open(self.file_path) as f:
            # Leemos los datos encriptados
            datos_encriptados = f.read()
            # Desencriptamos los datos
            datos_desencriptados = fernet.decrypt(datos_encriptados)
            # Convertimos los datos a formato json
            self.conexiones = json.loads(datos_desencriptados)
            

    def conexion_pg(self):
        try:
            pg_params = self.conexiones["postgresql"]
            conn_pg = psycopg2.connect(host=pg_params['server'], port=pg_params['port'], user=pg_params['user'], password=pg_params['password'], dbname=pg_params['database'])
            #cur_pg = conn_pg.cursor()
            #mb.showinfo("Conexion", "Conexion exitosa a PostgreSQL")
            return conn_pg
        except Exception as error_postgres:
            mb.showerror("Error", error_postgres)
            sys.exit()
            
    def conexion_sqlserver(self):
        try:
            sql_params = self.conexiones["sqlserver"]
            conn_sql = pyodbc.connect(f"DRIVER={{SQL Server}};SERVER={sql_params['server']};PORT={sql_params['port']};UID={sql_params['user']};PWD={sql_params['password']};DATABASE={sql_params['database']}")
            #cur_pg = conn_pg.cursor()
            #mb.showinfo("Conexion", "Conexion exitosa a PostgreSQL")
            return conn_sql
        except Exception as error_sqlserver:
            mb.showerror("Error", error_sqlserver)
            sys.exit()       
            
            
    def usuario_sistema(self):
        usuario_sist=self.conexiones["nomb_usuario"]
        usuario=usuario_sist['usuario']
        paswo=usuario_sist['pass']
        return usuario,paswo
    

    
    