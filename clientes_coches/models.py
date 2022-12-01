from django.db import models


# Create your models here.
class Cliente(models.Model):
    clientes = models.Manager()
    nombre = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=60)
    dni = models.CharField(max_length=9)
    email = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellidos} {self.dni} {self.email}"


class Coche(models.Model):
    matricula = models.CharField(max_length=20)
    marca = models.CharField(max_length=40)
    color = models.CharField(max_length=40)
    combustible = models.CharField(max_length=40)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.matricula} {self.marca} {self.color} {self.combustible} Del cliente: {self.id_cliente}"
