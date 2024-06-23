from librerias import *


class Datos_usuario:
    def __init__(self):
        self=self
        
        
    def usuario(self):
        return getuser()
    
    def nombre_pc(self):
        return socket.gethostname()