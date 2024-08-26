class CentrarVentana:
    def __init__(self, ventana):
        self.ventana = ventana

    def centrar(self):
        self.ventana.update_idletasks()
        ancho = self.ventana.winfo_width()
        alto = self.ventana.winfo_height()
        x = (self.ventana.winfo_screenwidth() // 2) - (ancho // 2)
        y = (self.ventana.winfo_screenheight() // 2) - (alto // 2)
        self.ventana.geometry(f'{ancho}x{alto}+{x}+{y}')
