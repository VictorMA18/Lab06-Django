from django.urls import path
from . import views

urlpatterns = [
    path('crearAlumno/', views.crear_alumno, name='crear_alumno'), 
    path('listaAlumno/', views.lista_alumnos, name='lista_alumnos'),
    path('crearCurso/', views.crear_curso, name='crear_curso'),
    path('listaCurso/', views.lista_cursos, name='lista_cursos') ,
    path('crearNota/', views.crear_nota, name='crear_nota'),
    path('listaNota/', views.lista_notas, name='lista_notas'),
]