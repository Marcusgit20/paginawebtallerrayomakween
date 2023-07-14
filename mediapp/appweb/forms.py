from django import forms
from .models import Contacto, Mecanico, Trabajo, Postulacion

class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = "__all__" # __all__ especifica que se van a usar todos los campos
        #fields = ["nombre", "email", "telefono"] En caso de que queramos especificar que campos vamos a usar
        
class MecanicoForm(forms.ModelForm):

    class Meta:
        model = Mecanico
        fields = "__all__"
    
        widgets = {
            "fecha_nacimiento" : forms.DateInput(attrs={'type': 'date'}, format=('%Y-%m-%d'))
        }


class TrabajoForm(forms.ModelForm):

    class Meta:
        model = Trabajo
        fields = "__all__"

        widgets = {
            "fecha_trabajo" : forms.DateInput(attrs={'type': 'date'}, format=('%Y-%m-%d'))
        }


class PostulacionForm(forms.ModelForm):

    class Meta:
        model = Postulacion
        fields = "__all__"