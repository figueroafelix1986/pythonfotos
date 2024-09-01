from django.shortcuts import render
from .models import Servicio

# Create your views here.


def service_home(request):

    return render(request, "ServiciowebApp/felix.html")


def servicio(request):

    list_servicio = Servicio.objects.all()
    return render(request, "ServiciowebApp/servicios.html", {'todo_servicios': list_servicio})
