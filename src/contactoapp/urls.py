from django.urls import path
from contactoapp.views import *


urlpatterns = [
    path('contacto/', contacto, name="contacto" ),
]