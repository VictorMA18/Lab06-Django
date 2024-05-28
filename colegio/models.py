from django.db import models

class Alumno(models.Model):
    nombre = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nombre

class Curso(models.Model):
    curso = models.CharField(max_length=100, unique=True)  
    def __str__(self):
        return self.curso

