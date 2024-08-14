from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import *
from django.core.mail import send_mail
from django.conf import settings
from gestionPedidos.forms import FormularioContacto

# Create your views here.

def busqueda_productos(request):
    
    return render(request, "busqueda_productos.html")


def buscar(request):
    nomb_articulo=request.GET['product']
    if (nomb_articulo):
        #mensaje=(f"Ariculo buscado:  '{nomb_articulo}'")
        
        articulos=Articulo.objects.filter(seccion__icontains=nomb_articulo)
        
        return render(request, "resultado_articulos.html",{"list_articulos":articulos,"query":nomb_articulo})
    else:
        mensaje="No hay articulos para mostrar"
    
    return HttpResponse(mensaje)

def contacto(request):
    if request.method=='POST':
        
        miFormulario=FormularioContacto(request.POST)
        
        if miFormulario.is_valid():
            infoFromulario=miFormulario.cleaned_data
            send_mail(infoFromulario['asunto'],infoFromulario['mensaje'],
                    infoFromulario.get('email',''),['figueroa.felix1986@gmail.com'])
            
            return render(request,'gracias.html')
        
    else:
        miFormulario=FormularioContacto()
        
    return render(request,'formulario_contacto.html', {"form": miFormulario})
    


"""def contacto(request):
    
    if request.method=='POST':
        
        subject=request.POST["asunto"]
        
        mesagge=request.POST["mensajes"]+" " +request.POST["nom_email"]
        
        email_from=settings.EMAIL_HOST_USER
        
        resipient_list =["figueroa.felix1986@gamilcom"]
        
        send_mail(subject,mesagge,email_from,resipient_list)
        
        
        return render(request,'gracias.html')
        
    
    return render(request,'contacto.html')"""