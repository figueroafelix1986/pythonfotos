from django.shortcuts import render

# Create your views here.


def tiendas(request):

    return render(request, "TiendawebApp/tienda.html")
