from django.forms import Form, CharField, FloatField, IntegerField, ImageField

class FormularioBusqueda(Form):
    nombre_producto = CharField(max_length=50)


class FormularioCargaProductos(Form):
    nombre =CharField(max_length=50)
    marca =CharField(max_length=50)
    precio =FloatField()
    stock =IntegerField()
    imagen_productos=ImageField()