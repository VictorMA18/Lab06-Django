from django.shortcuts import render, redirect
from .forms import AlumnoForm
from .models import ALumno
# Create your views here.
def crear_alumno(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_alumnos')
    else:
        form = AlumnoForm()
    return render(request, 'colegio/crear_alumno.html', {'form':form})

def lista_alumnos(request):
    alumnos = ALumno.objects.all()
    return render(request, 'colegio/lista_alumnos.html', {'alumnos': alumnos})