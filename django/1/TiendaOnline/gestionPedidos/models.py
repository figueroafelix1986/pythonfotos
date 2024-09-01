from django.db import models

# Create your models here.

class Clients(models.Model):
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=50, verbose_name="La direccion")
    #que no sea requerido
    email=models.EmailField(blank=True,null=True)
    telefono=models.CharField(max_length=7)
    
    def __str__(self):
        return self.nombre
    
class Articulo(models.Model):
    nombre=models.CharField(max_length=30)
    seccion=models.CharField(max_length=20)
    precio=models.IntegerField()
    
    def __str__(self):
        return f"El nombre es {self.nombre} la seccion es {self.seccion} y su precio es {self.precio}"
    
    
class Pedidos(models.Model):
    numero=models.IntegerField()
    fecha=models.DateField()
    entregado=models.BooleanField()


class Factura(models.Model):
    nombre = models.CharField(max_length=100)
    total = models.DecimalField(max_digits=10, decimal_places=2)


class Servicio(models.Model):
    factura = models.ForeignKey(
        Factura, related_name='servicios', on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=200)
    costo = models.DecimalField(max_digits=10, decimal_places=2)
