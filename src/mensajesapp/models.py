from django.db import models

# Create your models here.

class Mensaje(models.Model):

    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    fecha = models.DateTimeField(auto_now_add=True)
    mensaje = models.TextField()

    def __str__(self):

        return f"Nombre:{self.nombre},Email:{self.email} Fecha:{self.fecha} Mensaje:{self.mensaje}"