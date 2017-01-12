from django import forms

from .models import Registrado

class RegModelForm(forms.ModelForm):
	class Meta:
		model = Registrado
		fields = ["email", "nombre"]

	def clean_email(self): 
		email = self.cleaned_data.get("email")
		email_base, proveedor = email.split ("@")
		dominio, extension = proveedor.split(".") 
		if not extension == "edu":
			raise forms.ValidationError("Por favor utiliza una dirección válida")
		return email


class ContactForm(forms.Form):
	nombre = forms.CharField(required=False, max_length=100)
	email = forms.EmailField()
	mensaje = forms.CharField(widget=forms.Textarea)
