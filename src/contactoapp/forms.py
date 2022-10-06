from django import forms

class FormularioContacto(forms.Form):

    nombre=forms.CharField(max_length=50)
    email=forms.EmailField()
    contenido=forms.CharField(widget=forms.Textarea)