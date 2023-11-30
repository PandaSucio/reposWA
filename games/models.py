from django.db import models
from django.contrib.auth.models import User


class Desarrollador(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre


class Género(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Jugador(models.Model):
    cantidad = models.IntegerField()

    def __str__(self):
        return f"{self.cantidad} Jugadores"


class Juego(models.Model):
    titulo = models.CharField(max_length=255)
    desarrollador = models.ForeignKey(Desarrollador, on_delete=models.CASCADE)
    lanzamiento = models.DateField()
    genero = models.ForeignKey(Género, on_delete=models.CASCADE)
    jugadores = models.ForeignKey(Jugador, on_delete=models.CASCADE)
    portada_url = models.URLField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
