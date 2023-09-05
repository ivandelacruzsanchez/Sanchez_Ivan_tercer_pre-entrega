from django.shortcuts import render
from django.http import HttpResponse
from .models import curso, estudiante
# Create your views here.

def Curso(req, nombre, camada):
    Curso = curso(nombre=nombre, camada=camada)
    Curso.save()
    return HttpResponse(f"""
           <p>Curso:{Curso.nombre} - Camada {Curso.camada} agregado!</p>        
                        """)
    
def Estudiante(req, nombre, apellido):
    Estudiante = estudiante(nombre=nombre, apellido=apellido)
    Estudiante.save()
    return HttpResponse(f"""
           <p>Nombre:{Estudiante.nombre} - Apellido {Estudiante.apellido} agregado!</p>        
                        """)