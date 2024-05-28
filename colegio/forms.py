from django import form
from .models import ALumno

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