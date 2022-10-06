from django.db import models

# Create your models here.


class Productos(models.Model):
    nombre=models.CharField(max_length=70)
    marca=models.CharField(max_length=70)
    precio=models.FloatField()
    stock =models.IntegerField()
    imagen_productos=models.ImageField(upload_to="imagenes_productos", null=True)

    def __str__(self):
        return f"Producto:{self.nombre}, Marca:{self.marca}, Precio:${self.precio}" 