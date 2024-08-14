from django.shortcuts import render, HttpResponse
from ServiciowebApp.models import Servicio

# Create your views here.


def home(request):

    return render(request, "ProyectowebApp/home.html")


def servicio(request):

    list_servicio = Servicio.objects.all()
    return render(request, "ProyectowebApp/servicios.html", {'todo_servicios': list_servicio})


def tiendas(request):

    return render(request, "ProyectowebApp/tienda.html")


def blog(request):

    return render(request, "ProyectowebApp/blog.html")


def contacto(request):

    return render(request, "ProyectowebApp/contacto.html")
