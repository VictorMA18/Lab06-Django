from django.urls import path
from . import views

urlpatterns = [
    path('crear/', views.crear_alumno, name='crear_alumno'), 
    path('listar/', views.lista_alumnos, name='lista_alumnos'),  
]