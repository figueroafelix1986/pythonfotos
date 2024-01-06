# Importamos los módulos necesarios
from cryptography.fernet import Fernet
import json

# Función para generar la clave y guardarla en un archivo
def generar_clave():
    clave = Fernet.generate_key()
    with open("datos_", "wb") as archivo_clave:
        archivo_clave.write(clave)

# Función para cargar la clave desde el archivo
def cargar_clave():
    return open("datos_", "rb").read()

# Función para encriptar el fichero json
def encriptar_fichero(fichero_original, fichero_encriptado, clave):
    # Cargamos los datos del fichero json
    with open(fichero_original, "r") as f:
        datos = json.load(f)
    # Convertimos los datos a bytes
    datos_bytes = json.dumps(datos).encode()
    # Creamos el objeto Fernet con la clave
    fernet = Fernet(clave)
    # Encriptamos los datos
    datos_encriptados = fernet.encrypt(datos_bytes)
    # Guardamos los datos encriptados en el fichero de salida
    with open(fichero_encriptado, "wb") as f:
        f.write(datos_encriptados)

# Función para desencriptar el fichero json
def desencriptar_fichero(fichero_encriptado, fichero_desencriptado, clave):
    # Cargamos los datos encriptados del fichero
    with open(fichero_encriptado, "rb") as f:
        datos_encriptados = f.read()
    # Creamos el objeto Fernet con la clave
    fernet = Fernet(clave)
    # Desencriptamos los datos
    datos_desencriptados = fernet.decrypt(datos_encriptados)
    # Convertimos los datos a formato json
    datos = json.loads(datos_desencriptados)
    # Guardamos los datos desencriptados en el fichero de salida
    with open(fichero_desencriptado, "w") as f:
        json.dump(datos, f, indent=4)

# Generamos la clave
generar_clave()
# Cargamos la clave
clave = cargar_clave()
# Encriptamos el fichero json
encriptar_fichero("conexion.json", "datos_encriptados", clave)
# Desencriptamos el fichero json
#desencriptar_fichero("datos_encriptados", "datos_desencriptados", clave)
