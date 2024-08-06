import psycopg2

# Configuración de la conexión
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5436"  # Asegúrate de usar el puerto correcto para la versión 14
)

# Crear un cursor
cur = conn.cursor()

# Ejecutar la consulta para obtener la versión
cur.execute("SELECT version();")

# Obtener el resultado
version = cur.fetchone()

# Imprimir la versión
print(f"La versión de PostgreSQL es: {version[0]}")

# Cerrar la conexión
cur.close()
conn.close()

