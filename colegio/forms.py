from django import forms
from .models import Alumno, Curso, Nota

class AlumnoForm(forms.ModelForm):
    nombre = forms.CharField(max_length=255, label='Nombre del Alumno')

    class Meta:
        model = Alumno
        fields = ['nombre']

    def save(self, commit=True):
        alumno = super().save(commit=False)
        if commit:
            alumno.save()
        return alumno

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['curso']

class NotaForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields = ['alumno', 'curso', 'nota', 'nota2', 'nota3']