from django.urls import path
from .views import *

urlpatterns = [
    path('crear_curso/', crear_curso),
    path('listar_cursos/', listar_cursos),
    path('personal/', personal, name="personal"),
    path('equipos/', equipos, name="equipos"),
    path('oficinas/', oficinas, name="oficinas"),
    path('trabajos/', trabajos, name="trabajos"),
    path('formulario/', formulario, name="formulario"),
]