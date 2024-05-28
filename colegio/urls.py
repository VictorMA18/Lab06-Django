from django.urls import path
from . import views

urlpatterns = [
    path('crearAlumno/', views.crear_alumno, name='crear_alumno'), 
    path('listaAlumno/', views.lista_alumnos, name='lista_alumnos'),
    path('crearCurso/', views.crear_curso, name='crear_curso'),
    path('listaCurso/', views.lista_cursos, name='lista_cursos') ,
]