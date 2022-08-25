from django.shortcuts import render
from .models import Familia
from unicodedata import name
from datetime import datetime

def inicio(request):
    return render(request, 'inicio.html', context={})

def crear_miembro(request, nombre):
    nuevo_miembro_familia = Familia.objects.create(nombre=nombre, apellido="Unico", edad=25, fecha_nac=datetime.date, tel_mov=541199220)
    context = {'familia':nuevo_miembro_familia}
    return render(request, 'agregar.html', context)

def lista_miembros(request):
    miembros_familia = Familia.objects.all()
    context = {'familia':miembros_familia}
    return render(request, "listado.html", context)