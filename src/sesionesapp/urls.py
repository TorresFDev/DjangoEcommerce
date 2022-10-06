from django.forms import Form, CharField, FloatField, IntegerField, EmailField,PasswordInput, ImageField
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib.auth.models import User

class EditarUsuarioForm(UserCreationForm):

    email= EmailField()
    password1= CharField(label="Contraseña", widget=PasswordInput)
    password2= CharField(label="Confirmar Contraseña", widget=PasswordInput)

    class Meta:
        model= User
        fields = ["email", "password1", "password2"]
        help_texts = {"email":"", "password1":"", "password2":""}



class CambiarContraseña(PasswordChangeForm):

    class Meta:
        model = User
        fields = '__all__'



class AvatarForm(Form):
    imagen = ImageField()