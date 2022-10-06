
from django.urls import path, include
from mensajesapp.views import *


urlpatterns = [
    path("nosotros/", nosotros, name="nosotros"), 
    path("mensajes/", MensajeCrear.as_view(), name="mensajes"), 
    path("mensaje_editar/<pk>", MensajeEditar.as_view(), name="mensaje_editar"), 
    path("mensaje_list/", MensajeList.as_view(), name="mensaje_list"),
    path("mensaje_detail/<pk>", MensajeDetail.as_view(), name="mensaje_detail"), 
    path("mensaje_borrar/<pk>", MensajeBorrar.as_view(), name="mensaje_borrar")
]