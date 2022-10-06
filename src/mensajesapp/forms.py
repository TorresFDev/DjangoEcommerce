from django.forms import Form, CharField, FloatField, IntegerField, ImageField
from mensajesapp.models import Mensaje
from django import forms


class MensajeForm(forms.ModelForm):

    class Meta:
        model = Mensaje
        fields = '__all__'