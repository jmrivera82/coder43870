from django.shortcuts import render
from django.http import HttpResponse
from .models import curso

# Create your views here.

def crear_curso(request):
    nombre_curso="programacion basica"
    comision_curso=112233
    print("creando curso")
    cursada=curso(nombre=nombre_curso, comision=comision_curso)
    cursada.save()
    respuesta=f"Curso creado: {cursada.nombre} - {cursada.comision}"
    return HttpResponse(respuesta)

def listar_cursos(request):
    cursos=curso.objects.all()
    respuesta=""
    for curso in cursos:
        respuesta+=f"{curso.nombre} - {curso.comision} <br>"
    return HttpResponse(respuesta)

