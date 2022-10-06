from django.shortcuts import render, redirect
from django.http import HttpResponse
from sesionesapp.forms import *
from sesionesapp.models import Avatar
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.models import User
# Create your views here.


def iniciar_sesion(request):

    if request.method == "GET":
        formulario = AuthenticationForm()

        context={
            "form": formulario}

        return render(request, "sesionesapp/login.html", context)

    else:
        formulario = AuthenticationForm(request, data=request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            usuario = authenticate (username=data.get("username"), password=data.get("password"))
            
            if usuario is not None:
                login (request, usuario)
                
                return redirect ("index")
            
            else:
                context={
                    "form" : formulario}

                return render(request, "sesionesapp/login.html", context)

        else:
            context={
                "error": "Formulario No  Valido",
                "form" : formulario}

            return render(request, "sesionesapp/login.html", context)


def registro_usuario(request):
    if request.method =="GET":
        formulario = UserCreationForm()
        return render (request, "sesionesapp/registro.html", {"form": formulario})
    else:
        formulario= UserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect ("productos")
        else:
            return render (request, "sesionesapp/registro.html", {"form": formulario, "error":"Formulario  NO valido"})


@login_required
def cambiar_contrasenia(request):
    
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)

        if form.is_valid():

            usuario = form.save()
            update_session_auth_hash(request, usuario)

            return redirect('iniciar_sesion')
        
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'sesionesapp/cambiar_contrasenia.html', {'form': form})

@login_required
def agregar_avatar(request):

    if request.method == 'GET':
        form = AvatarForm()
        contexto = {'form':form}
        return render(request, 'sesionesapp/agregar_avatar.html', contexto)
    else:
        form = AvatarForm(request.POST, request.FILES)

        if form.is_valid():
            data = form.cleaned_data
            usuario = User.objects.filter(username = request.user.username).first()
            avatar = Avatar(usuario = usuario, imagen = data['imagen'])
            avatar.save()
            return redirect('index')