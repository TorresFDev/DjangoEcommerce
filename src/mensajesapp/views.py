
from django.shortcuts import render, redirect
from django.http import HttpResponse
from mensajesapp.models import *
from django.views.generic import ListView, DetailView ,CreateView, UpdateView, DeleteView

# Create your views here.

def nosotros(request):
    return render (request, "mensajesapp/nosotros.html")

class MensajeList(ListView):
    model=Mensaje
    tamplate_name ="/mensajesapp/mensaje_list.html"

class MensajeDetail(DetailView):
    model=Mensaje
    tamplate_name ="/mensajesapp/mensaje_detail.html"

class MensajeCrear(CreateView):
    model=Mensaje
    success_url ="/mensaje_list"
    fields = ["nombre", "email" , "mensaje"]

class MensajeEditar(UpdateView):
    model=Mensaje
    success_url ="/mensaje_list"
    fields = ["nombre", "email" , "mensaje"]

class MensajeBorrar(DeleteView):
    model=Mensaje
    success_url ="/mensaje_list"