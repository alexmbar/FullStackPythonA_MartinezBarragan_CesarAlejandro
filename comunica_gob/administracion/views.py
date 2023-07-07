from django.db import IntegrityError
from django.shortcuts import redirect, render, HttpResponse,  get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import SignupForm, ReportForm, LoginForm
from .models import Reportes


def login_forbidden(user):
    return not user.is_authenticated

# Create your views here.
# @login_required
# @user_passes_test(login_forbidden, 1='home')
def index(request):
    return render(request, 'index.html',{
        'title': "Inicio"})

#@login_required
def home(request):
    # context ={}
    # persona = Personas.objects.get(usuario__pk=request.user.pk)
    # context['persona'] = persona
    return render(request, 'home.html',
    #context, 
        {
        'title': "Reportes"
        })

# @login_required
# def reporte1(request):
#     if request.POST["reporte"]:
#         return render(request, 'reporte.html',{
#             'title': "Crear Reporte"
#         })
#     if request.method == 'GET':
#         return render(request, 'reporte.html',{
#             'title':"Entro en else"
#         })


# @login_required
# def reporte(request):
#     if request.method == 'POST':
#         reporte_value = request.POST.get("reporte", None)
#         if reporte_value == 'reparacion':
#             return render(request, 'reporte.html', {
#                 'title': "Crear reporte de reparacion de calles y aceras" ,
#                 "form": ReportForm(),         
#             })
#         elif reporte_value == 'recoleccion':
#             return render(request, 'reporte.html', {
#                 'title': "Crear reporte de recolección de basura y residuos" ,
#                 "form": ReportForm(),         
#             })
#         elif reporte_value == 'mantenimiento':
#             return render(request, 'reporte.html', {
#                 'title': "Crear reporte de mantenimiento de parques y alumbrado público" ,
#                 "form": ReportForm(),         
#             })
#         elif reporte_value == 'gestion':
#             return render(request, 'reporte.html', {
#                 'title': "Crear reporte de gestión de emergencias a desastres naturales" ,
#                 "form": ReportForm(),         
#             })
#         else:
#             return render(request, 'reporte.html', {
#                 'title': "reporte_value",
#                 "form": ReportForm(),         
#             })
#     elif request.method == 'GET':
#         return redirect('home')

@login_required
def reporte(request):
    title_mapping = {
        'reparacion': "Crear reporte de reparacion de calles y aceras",
        'recoleccion': "Crear reporte de recolección de basura y residuos",
        'mantenimiento': "Crear reporte de mantenimiento de parques y alumbrado público",
        'gestion': "Crear reporte de gestión de emergencias a desastres naturales",
    }

    default_title = "Seleccione un tipo de reporte"

    if request.method == 'POST':
        reporte_value = request.POST.get("reporte", None)
        title = title_mapping.get(reporte_value, default_title)
        form = ReportForm(request.POST)
        if form.is_valid():
            reporte = form.save(commit=False)
            reporte.tipo_reporte = title  # Asignar el valor de "title" al campo "tipo_reporte"
            reporte.save()
            return redirect('home')
    else:
        reporte_value = request.GET.get("reporte", None)
        title = title_mapping.get(reporte_value, default_title)
        form = ReportForm()
    return render(request, 'reporte.html', {
        'title': title,
        'form': form,
    })

def signup(request):
    form = SignupForm(request.POST)
    user = None  # Asignar None al comienzo de la función

    if request.method == 'GET':
        return render(request, 'signup.html', {
            "form": form,
            'title': "Registrarse",
            'messages': messages.get_messages(request),
        })
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                if form.is_valid():
                    user = form.save()
                if user is not None:  # Verificar si user se ha asignado correctamente
                    login(request, user)
                    return redirect('home')
                else:
                    messages.warning(request, 'Usuario ya existe.')
                    return render(request, 'signup.html', {
                        "form": form,
                        'title': "Registrarse",
                        'messages': messages.get_messages(request),
                    })
            except IntegrityError:
                messages.warning(request, 'Usuario ya existe.')
                return render(request, 'signup.html', {
                    "form": form,
                    'title': "Registrarse",
                    'messages': messages.get_messages(request),
                })
        else:
            messages.warning(request, 'Contraseña no coincide.')
            return render(request, 'signup.html', {
                "form": form,
                'title': "Registrarse",
                'messages': messages.get_messages(request),
            })


@login_required
def signout(request):
    logout(request)
    return redirect('index')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {"form": LoginForm(),
        'title': "Iniciar sesión"})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        # print(request.POST['username'])
        # print (request.POST['password'])
        if user is None:
            messages.warning(request, 'Usuario/Contraseña no valido.')
            return render(request, 'signin.html', {"form": LoginForm(),
            'title': "Inicia sesión"})

        login(request, user)
        return redirect('home')