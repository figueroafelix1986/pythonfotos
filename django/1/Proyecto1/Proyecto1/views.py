from django.http import HttpResponse
import datetime
from django.template import Template, Context, loader
from django.shortcuts import render

class Persona(object):
    def __init__(self,nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido
        self.fecha_actual=datetime.datetime.now()

p1=Persona ("felix","primero")

def saludo(request):    
    
    nombre=p1.nombre
    
    apellidos=p1.apellido
    
    fecha_actual =p1.fecha_actual
    
    temas_curso=["plantilla","modelos","fromulario","vista"]
    

    #with open("E:/GITHUB/django/1/Proyecto1/Proyecto1/plantilla/plantilla1.html", "r") as archivo:
    #    doc_externo = archivo.read()
    #doc_externo=open("E:/GITHUB/django/1/Proyecto1/Proyecto1/plantilla/plantilla1.html")    
    #plt=Template(doc_externo.read())    
    #doc_externo.close()
    
    ##doc_externo=loader.get_template('plantilla1.html')
    
    #ctx=Context({"nombre_person":nombre,"apellido_person":apellidos,"fecha":fecha_actual, "temas":temas_curso})
    ctx=({"nombre_person":nombre,"apellido_person":apellidos,"fecha":fecha_actual, "temas":temas_curso})
    
    ##variable=doc_externo.render(ctx)
    
    return render(request, "plantilla1.html",ctx)

def cursos(request):

    ctx=({"dame_fecha":p1.fecha_actual})
    return render(request, "Cursos.html",ctx)


def cursos1(request):

    return render(request, "Cursos1.html")

def despedida(request):
    variable='me voy django'
    
    return HttpResponse(variable)

def dame_Fecha(request):
    fecha_actual =datetime.datetime.now()
    
    variable=f"""<html>
    <body>
    <h1>
    Fecha actual {fecha_actual}
    </h1>
    </body>
    </html>"""
    return HttpResponse(variable)


def calcularEdad(request, edadActual,agno):
    
    #edadActual=18
    periodo=agno-2024
    edadFutura=edadActual+periodo
    variable=f"""<html>
    <body>
    <h1>
    La edad futura seria {edadFutura}
    </h1>
    </body>
    </html>"""
    return HttpResponse(variable)