from django.db import IntegrityError
from django.shortcuts import redirect, render, HttpResponse,  get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import SignupForm, ReportForm, LoginForm, PersonasForm
from .models import Reportes, Personas


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
    context ={}
    persona = Personas.objects.get(usuario__pk=request.user.pk)
    context['persona'] = persona
    context['title'] = "Reportes"
    return render(request, 'home.html',context)

def misreportes(request):
    user = request.user
    reportes = Reportes.objects.filter(persona__usuario=user)
    return render(request, 'misreportes.html', {'reportes': reportes})

def reporte(request):
    if request.method == 'POST':
        reporte_value = request.POST.get("reporte", None)
        form = ReportForm(request.POST)
        if reporte_value == 'reparacion':
            form_title = "Crear reporte de reparacion de calles y aceras"
        elif reporte_value == 'recoleccion':
            form_title = "Crear reporte de recolección de basura y residuos"
        elif reporte_value == 'mantenimiento':
            form_title = "Crear reporte de mantenimiento de parques y alumbrado público"
        elif reporte_value == 'gestion':
            form_title = "Crear reporte de gestión de emergencias a desastres naturales"

        if form.is_valid():
            report = form.save(commit=False)
            persona = Personas.objects.get(usuario=request.user)
            report.persona = persona  
            #report.tipo_reporte = tipo_reporte
            report.save()
            return redirect('home')
    else:
        return redirect('home')
        form_title = "reporte_value"
        form = ReportForm()
    
    return render(request, 'reporte.html', {
        'title': form_title,
        'form': form,
        'tipo_reporte': reporte_value,
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
                # if user is not None:  # Verificar si user se ha asignado correctamente
                #     login(request, user)
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

@login_required
def verperfil(request):
    usuario = request.user
    persona = Personas.objects.get(usuario=usuario)
    
    if request.method == 'POST':
        form = PersonasForm(request.POST, instance=persona)
        if form.is_valid():
            form.save()
            return redirect('verperfil')
    else:
        form = PersonasForm(instance=persona)
    
    return render(request, 'verperfil.html', {'form': form})