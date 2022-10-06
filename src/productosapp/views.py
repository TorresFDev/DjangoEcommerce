from django.shortcuts import render, redirect
from django.http import HttpResponse
from sesionesapp.models import Avatar
from productosapp.models import *
from productosapp.forms import FormularioBusqueda,FormularioCargaProductos
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
   
    return render(request, "productosapp/index.html")


def productos(request):
    
    listado_productos=Productos.objects.all()

    if request.GET.get("nombre_producto"):

        formulario=FormularioBusqueda(request.GET)

        if formulario.is_valid():
            data=formulario.cleaned_data
            listado_productos=Productos.objects.filter(nombre__icontains= data["nombre_producto"])

        return render (request, "productosapp/productos.html",{"productos": listado_productos, "formulario": formulario})

    else:
        formulario=FormularioBusqueda()
        return render (request, "productosapp/productos.html",{"productos": listado_productos, "formulario": formulario})

@login_required
def cargar_productos(request):

    if request.method == "GET":
        formularioCarga=FormularioCargaProductos()
        return render(request, "productosapp/cargar_productos.html",{"formularioCarga":formularioCarga} )
    else:
        formularioCarga=FormularioCargaProductos(request.POST, request.FILES)
        if formularioCarga.is_valid():
            data = formularioCarga.cleaned_data
            
            producto = Productos(
                nombre= data.get("nombre"),
                marca= data.get("marca"),
                precio= data.get("precio"),
                stock= data.get("stock"),
                imagen_productos= data.get("imagen_productos"),
                )
            producto.save()
            formularioCarga=FormularioCargaProductos()
            return redirect ("index")

        
        return render(request, "productosdapp/cargar_productos.html",{"formularioCarga":formularioCarga, "errors":"formulario no valido"} )

@login_required
def borrar_productos(request, id_producto):
    try:
        producto=Productos.objects.get(id=id_producto)
        producto.delete()
        return redirect( "productos")
    except:
        return HttpResponse(f"error, no se pudo borrar el curso: {id_producto}")

@login_required
def editar_productos(request, id_producto):

    if request.method == "GET":
        formulario=FormularioCargaProductos()
        contexto={
            "formulario":formulario
        }

        return render(request, "productosapp/editar_productos.html", contexto)
    
    
    else:
        formulario=FormularioCargaProductos(request.POST, request.FILES)
        if formulario.is_valid():
            data=formulario.cleaned_data

            try:
                producto=Productos.objects.get(id=id_producto)

                producto.nombre=data.get("nombre")
                producto.marca=data.get("marca")
                producto.precio=data.get("precio")
                producto.stock=data.get("stock")
                producto.imagen_productos=data.get("imagen_productos")

                producto.save()

            except:
                return HttpResponse("se ha producido un error.")

        formulario=FormularioCargaProductos()
        producto=Productos.objects.all()


        return redirect("productos")