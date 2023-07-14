from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactoForm, MecanicoForm, TrabajoForm, PostulacionForm
from .models import Mecanico, Trabajo, Postulacion
from django.contrib.auth.models import User,Group
from django.contrib.auth import authenticate, login

# Create your views here.
def home(request):
    return render(request, "home.html")

def contacto(request):
    data = {
        'form': ContactoForm,
        'mensaje': ""
    }

    if request.method == "POST":
        formulario = ContactoForm(data=request.POST)

        if formulario.is_valid():
            formulario.save()
            data['mensaje'] ="Contacto guardado"
        else:
            data['form'] = formulario
            data['mensaje'] = "Ocurrio un error"

    return render(request, "contacto.html", data)

def galeria(request):
    return render(request, "galeria.html")

def login(request):
    return render(request, "registration/login.html")

def user_login(request):
    return redirect(to='administrador')

def mecanicos(request):
    mecanicos = Mecanico.objects.all()
    data = {
        'mecanicos': mecanicos
    }
    return render(request, "mecanicos.html", data)

def escaneo(request):
    return render(request, "escaneo.html")

def cambiofrenos(request):
    return render(request, "cambiofrenos.html")

def mantencion(request):
    return render(request, "mantencion.html")

def paginamecanico(request):

    data = {
        'form' : TrabajoForm,
        'mensaje' : ""
    }

    if request.method == "POST":
        formulario = TrabajoForm(data=request.POST, files=request.FILES)

        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = formulario
            data['mensaje'] = "Trabajo Agregado"
    return render(request, "paginamecanico.html", data)

def administrador(request):

    mecanicos = Mecanico.objects.all()
    postulacion = Postulacion.objects.all()

    data = {
        'form' : MecanicoForm,
        'mensaje' : "",
        'mecanicos': mecanicos,
        'postulacion' : postulacion
    }

    if request.method == "POST":
        formulario = MecanicoForm(data=request.POST, files=request.FILES)

        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = formulario
            data['mensaje'] = "Mecanico Agregado"

    return render(request, "admin.html", data)

def listar_mecanico(request):

    mecanicos = Mecanico.objects.all()

    data = {
        'mecanicos': mecanicos
    }

    return render(request, "mantenedor/mecanico/listar.html", data)


def modificar_mecanico(request, rut):
    mecanico = get_object_or_404(Mecanico, rut=rut)

    data = {
        "form" : MecanicoForm(instance=mecanico)
    }

    if request.method == "POST":
        formulario = MecanicoForm(data=request.POST, instance=mecanico, files=request.FILES)

        if formulario.is_valid():
            formulario.save()
            return redirect(to="administrador")
        else:
            data['form'] = formulario
            data['mensaje'] = "Ocurrio un error"
 
    return render(request, "mantenedor/mecanico/modificar.html", data)

def eliminar_mecanico(request, rut):
    mecanico = get_object_or_404(Mecanico, rut=rut)

    mecanico.delete()

    return redirect(to=administrador)

# def listar_trabajos(request):

#     trabajo = Trabajo.objects.all()

#     data = {
#         'trabajo': trabajo
#     }

#     return render(request, "mantenedor/mecanico/admin.html", data)

def registro_mecanico(request):
    return render(request, "registration/registro.html")

def listar_trabajo(request):
    trabajos = Trabajo.objects.all()

    data = {
        'trabajos': trabajos
    }
    return render(request, "jobs/listar.html", data)


def postulacion(request):
    data = {
        'form' : PostulacionForm,
        'mensaje' : "",
    }

    if request.method == "POST":
        formulario = PostulacionForm(data=request.POST, files=request.FILES)

        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = formulario
            data['mensaje'] = "Postulacion Agregada"
    return render(request, "postulacion.html", data)

def eliminar_postulacion(request, rut_postulante):
    postulacion = get_object_or_404(Postulacion, rut_postulante=rut_postulante)

    postulacion.delete()

    return redirect(to=administrador)