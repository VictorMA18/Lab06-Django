from django.db import models

class Alumno(models.Model):
    nombre = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nombre

class Curso(models.Model):
    curso = models.CharField(max_length=100, unique=True)  
    def __str__(self):
        return self.curso

class Nota(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    nota = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    nota2 = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    nota3 = models.DecimalField(max_digits=4, decimal_places=2, default=0)