from pyexpat import model
from django.db import models

class Familia(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    fecha_nac = models.DateField(auto_now_add=True)
    tel_mov = models.IntegerField()