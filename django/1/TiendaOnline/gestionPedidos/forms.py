from django import forms
from .models import Factura, Servicio
from django.forms import inlineformset_factory

class FormularioContacto(forms.Form):
    asunto=forms.CharField()
    email=forms.EmailField()
    mensaje=forms.CharField()


class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = ['nombre', 'total']


ServicioFormSet = inlineformset_factory(
    Factura, Servicio, fields=['descripcion', 'costo'], extra=2)
