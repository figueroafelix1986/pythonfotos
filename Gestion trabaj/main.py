from view.view_menu import *
from ttkthemes import ThemedTk


# Crear la ventana principal
root = tk.Tk()

# Crear una instancia de la clase AplicacionMenu
app = AplicacionMenu(root)

# Iniciar el bucle principal de la aplicación
root.mainloop()