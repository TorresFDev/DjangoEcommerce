from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Avatar(models.Model):

    usuario = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)

    def __str__(self):
        return str(self.usuario)