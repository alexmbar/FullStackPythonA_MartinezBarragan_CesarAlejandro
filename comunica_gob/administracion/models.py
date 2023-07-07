from django.db import models
from django.contrib.auth.models import User
from .choices import ESTADOS_CHOICES

#class Estados(models.Model):
    # id = models.AutoField(primary_key=True)
    # clave = models.CharField(max_length=2, null=True)
    # estado = models.CharField(max_length=50)
    # pais = models.CharField(max_length=50)
    #Choiceestado = models.CharField(max_length=2, choices=ESTADOS_CHOICES)


class Personas(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    edad = models.IntegerField()
    calle = models.CharField(max_length=100)
    numero = models.IntegerField(null=True)
    colonia = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100, default='Chihuahua')
    email = models.CharField(max_length=100, null=True)
    codigo_postal = models.CharField(max_length=5)
    estado = models.CharField(
        max_length = 100,
        choices = ESTADOS_CHOICES,
        default = '1'
        )
    estatus = models.CharField(max_length=1, default='A')
    
    def __str__(self):
        return str(self.nombre)

# class TipoReporte(models.Model):
#     id = models.AutoField(primary_key=True)
#     nombre = models.CharField(max_length=100)
#     estatus = models.CharField(max_length=1, default='A')

#     def __str__(self):
#         return self.nombre

class Reportes(models.Model):
    id = models.AutoField(primary_key=True)
    persona = models.ForeignKey(Personas, on_delete=models.CASCADE,null=True)
    calle = models.CharField(max_length=100)
    numero = models.IntegerField(null=True)
    colonia = models.CharField(max_length=100)
    estado = models.CharField(
        max_length = 100,
        choices = ESTADOS_CHOICES,
        default = '1'
        )    
    ciudad = models.CharField(max_length=100, null=True)
    codigo_postal = models.CharField(max_length=10)
    tipo_reporte =models.CharField(max_length=100)
    #tipo_reporte = models.ForeignKey(TipoReporte, on_delete=models.CASCADE)
    estatus = models.CharField(max_length=1, default='A')
    descripcion = models.CharField(max_length=250, null=True)

    def __str__(self):
        return f"Reporte {self.id}"
