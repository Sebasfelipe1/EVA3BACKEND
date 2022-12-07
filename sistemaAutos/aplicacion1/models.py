from django.db import models

# Create your models here.

class Auto(models.Model):
     marca_auto = models.CharField(max_length=50)
     ruedas = models.CharField(max_length=2)
     puertas = models.CharField(max_length=2)
     patente = models.CharField(max_length=10)
     dueño_auto = models.CharField(max_length=50)
     rut_dueño = models.CharField(max_length=10)
     
class PersonalRRHH(models.Model):
     nombre_personal = models.CharField(max_length=20)
     apellido_parterno = models.CharField(max_length=20)
     apellido_materno = models.CharField(max_length=20)
     rut = models.CharField(max_length=10)
     sector = models.CharField(max_length=20)
     seccion = models.CharField(max_length=20)
     
class Cliente(models.Model):
     nombre_cliente = models.CharField(max_length=20)
     apellidoP_cliente = models.CharField(max_length=20)
     apellidoM_cliente = models.CharField(max_length=20)
     rut = models.CharField(max_length=10)
     edad = models.CharField(max_length=10)
     telefono = models.CharField(max_length=13)
     
     
     
     
     
     