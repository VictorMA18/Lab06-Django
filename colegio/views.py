from django.shortcuts import render, redirect
from .forms import AlumnoForm, CursoForm
from .models import Alumno, Curso
# Create your views here.
def crear_alumno(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_alumnos')
    else:
        form = AlumnoForm()
    return render(request, 'colegio/crear_alumno.html', {'form': form})

def lista_alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, 'colegio/lista_alumnos.html', {'alumnos': alumnos})

def crear_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_cursos')
    else:
        form = CursoForm()
    return render(request, 'colegio/crear_curso.html', {'form':form})

def lista_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'colegio/lista_cursos.html', {'cursos': cursos})