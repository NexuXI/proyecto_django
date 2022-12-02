from django.db import models


# Create your models here.
class Jugador(models.Model):
    jugadores = models.Manager()
    nombre = models.CharField(max_length=50)
    equipo = models.CharField(max_length=60)
    edad = models.IntegerField()
    nacionalidad = models.CharField(max_length=50)
    posicion = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.nombre} originario de: {self.nacionalidad} tiene {self.edad} años. Juega con: {self.equipo},  como: {self.posicion}."
