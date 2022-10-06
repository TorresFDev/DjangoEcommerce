
from django.urls import path, include
from productosapp.views import *


urlpatterns = [
    path("", index , name="index"),
    path('', include("sesionesapp.urls")),
    path("productos/", productos , name="productos"),
    path("cargar_productos/", cargar_productos , name="cargar_productos"),
    path("productos/borrar/<id_producto>", borrar_productos, name="borrar_productos"),
    path("productos/editar/<id_producto>", editar_productos, name="editar_productos")
]