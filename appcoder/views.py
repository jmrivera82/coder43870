from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.contrib import admin


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

def inicio(request):
	return render(request,"appcoder/inicio.html")

#def cursos(request):
#    return render(request,"appcoder/cursos.html")

def oficinas(request):
    return render(request, "appcoder/oficinas.html")

def personal(request):
    if request.method=="POST":
        pass
    else:
        personas=Personal.objects.all()
        return render(request,"appcoder/personal.html", {"personal":personas})

def equipos(request):
	return render(request,"appcoder/equipos.html")

def trabajos(request):
	return render(request,"appcoder/trabajos.html")

def formulario(request):
    if request.method=="POST":
        nombre=request.POST["nombre"]
        ubicacion=request.POST["ubicacion"]
        oficina=oficinas(nombre=nombre,ubicacion=ubicacion)
        oficina.save()
        return render(request,"appcoder/formulario.html", {"Mensaje":"Oficina creada"})
    
    else:
        return render(request,"appcoder/formulario.html")
    
    
    