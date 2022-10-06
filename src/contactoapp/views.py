from ast import For
from django.shortcuts import render, redirect
from django.http import HttpResponse
from contactoapp.forms import FormularioContacto
from django.core.mail import send_mail
from django.template.loader import render_to_string

# Create your views here.


def contacto(request):
    if request.method == "POST":
        form = FormularioContacto(request.POST)

        if form.is_valid():
            nombre=form.cleaned_data["nombre"]
            email= form.cleaned_data["email"]
            contenido=form.cleaned_data["contenido"]

            html=render_to_string("contactoapp/emails/contactoform.html",
            {"nombre":nombre,
            "email": email,
            "contenido":contenido})


            send_mail("nombre", "prueba2","example@gmail.com",['torresfdev@gmail.com'], html_message=html)
            return redirect ("index")

    else:
        form = FormularioContacto()

    return render(request,"contactoapp/contacto.html", {"form":form})