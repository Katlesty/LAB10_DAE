from django.db import models

class Producto(models.Model):
    codigoProducto = models.AutoField(max_length=11,primary_key=True)
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=18, decimal_places=2)

    def __str__(self):
        return self.nombre

class Venta(models.Model):
    codigoVenta = models.AutoField(max_length=11,primary_key=True)
    cliente = models.CharField(max_length=100)
    fecha = models.DateTimeField()

    def __str__(self):
        return self.cliente

class DetalleVenta(models.Model):
    venta = models.ManyToManyField('Venta')
    producto = models.ManyToManyField('Producto')
    cantidad = models.DecimalField(max_digits=18,decimal_places=2)
    descuento = models.DecimalField(max_digits=18,decimal_places=2)


