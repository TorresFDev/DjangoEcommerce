
from django.urls import path
from sesionesapp.views import *

from django.contrib.auth.views import LogoutView

urlpatterns = [
   
    
    path("iniciar_sesion/", iniciar_sesion, name="iniciar_sesion"),
    path("cambiar_contrasenia/",cambiar_contrasenia, name="cambiar_contrasenia"),
    path("registro/", registro_usuario, name="registro"),
    path("logout/", LogoutView.as_view(template_name="sesionesapp/logout.html"), name="logout"),
    path("agregar_avatar/",agregar_avatar, name="agregar_avatar"),
     ]