from django.db import models

class Estudiantes(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    camada = models.IntegerField()
    
class Profesores(models.Model):
    nombre = models.CharField(max_length=100)
    description = models.TextField()
    
    
class Trabajos(models.Model):
    estado = models.CharField(max_length=100)