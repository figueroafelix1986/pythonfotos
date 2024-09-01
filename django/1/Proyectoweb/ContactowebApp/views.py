from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import FromularioContacto

from django.core.mail import EmailMessage

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# Create your views here.


class SendCorreos:
    def __init__(self,  mensaje, usuario_correo, password, destinatario):
        self.mensaje = mensaje
        self.destinatario = destinatario
        self.usuario_correo = usuario_correo
        self.password = password

    def enviar_correo(self):
        dominio = '@eti.biocubafarma.cu'
        remitente = self.usuario_correo+"@eti.biocubafarma.cu"
        # destinatario = "felix.valdes@eti.biocubafarma.cu"
        try:
            msg = MIMEMultipart('alternative')
            msg['Subject'] = "Esto es para el pago"
            msg["From"] = remitente
            # msg["To"] = destinatario

            # Adjuntar el contenido HTML
            html_content = MIMEText(self.mensaje, 'html')
            msg.attach(html_content)

            # Enviar el correo
            with smtplib.SMTP('correo.eti.biocubafarma.cu') as server:
                server.starttls()
                server.login(self.usuario_correo+dominio, self.password)
                server.sendmail(remitente, self.destinatario, msg.as_string())
        except Exception as e:
            print(f"Error al enviar el correo: {e}")


def contacto(request):
    formulario_contacto = FromularioContacto()

    if request.method == "POST":
        formulario_contacto = FromularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            contenido = request.POST.get("contenido")

        # datos_email = EmailMessage(
        #     "Mensaje desde Django", f"El usuario {nombre} con la direccion {email} lo siguiente:\n\n {contenido} ", "", ["felix.valdes@eti.biocubafarma.cu"], reply_to=[email])

            datos_email = SendCorreos(
                contenido, "felix.valdes", "Eti*+072024", email)
            try:
                datos_email.enviar_correo()
            # messages.success(request, '¡Datos insertados correctamente!')
                return redirect("/contacto/?valido")
            except Exception as e:
                print(e)
                return redirect(f"/contacto/?NO")

    return render(request, "ContactowebApp/contacto.html", {'m_formulario': formulario_contacto})
