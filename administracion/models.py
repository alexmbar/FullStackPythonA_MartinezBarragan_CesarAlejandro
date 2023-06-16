from django.db import models
from django.contrib.auth.models import User

class Personas(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    edad = models.IntegerField()
    calle = models.CharField(max_length=100)
    colonia = models.CharField(max_length=100)
    codigo_postal = models.CharField(max_length=5)
    estado = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.nombre)