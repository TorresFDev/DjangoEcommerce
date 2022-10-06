from django.db import models

# Create your models here.
class FormularioContacto(models.Model):

    nombre=models.CharField(max_length=50)
    email=models.EmailField()
    fecha=models.DateTimeField(auto_now_add=True)
    contenido=models.CharField(max_length=250)


    def __str__(self):

        return f"Nombre:{self.nombre},Email:{self.email} Fecha:{self.fecha} Mensaje:{self.contenido}"