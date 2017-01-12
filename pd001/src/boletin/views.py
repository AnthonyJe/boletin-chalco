from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

from .forms import  RegModelForm, ContactForm
from .models import Registrado

# Create your views here.
def inicio(request):
	titulo = "Disfruta del site"
	if request.user.is_authenticated():
		titulo = "%s" %(request.user) 
	form = RegModelForm(request.POST or None)
	context = {
		"el_titulo": titulo,
		"el_form": form,
	}
	if form.is_valid():
		instance = form.save(commit=False)
		if not instance.nombre:
			instance.nombre="PERSONA"
		instance.save()

		context = {
			"el_titulo": "Gracias %s!" %(instance.nombre)
		}
		print (instance)
		print (instance.timestamp)
		"""
		form_data = form.cleaned_data
		mail = form_data.get('email')
		name = form_data.get('nombre')
		obj = Registrado.objects.create(email=mail, nombre=name)
		"""
	
	return render(request, "inicio.html", context)

def contact(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		email = form.cleaned_data.get("email")
		mensaje = form.cleaned_data.get("mensaje")
		nombre = form.cleaned_data.get("nombre")
		asunto = 'Form de Contacto'
		email_from = settings.EMAIL_HOST_USER
		email_to = [email_from, "jesus_omega97@hotmail.com", "anjeda@yahoo.com"]
		mensaje_email = "%s: %s enviado por: %s " %(nombre, mensaje, email)
		send_mail(asunto,
			mensaje_email,
			email_from,
			email_to,
			fail_silently=True 
			)

	context = {
		"form": form,
	}

	return render(request,"forms.html",context)
