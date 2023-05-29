from django.db import IntegrityError
from django.shortcuts import redirect, render, HttpResponse
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import LoginForm

# Create your views here.
def index(request):
    return render(request, 'index.html',{
        'title': "Inicio"})

@login_required
def home(request):
    return render(request, 'home.html',{
        'title': "Home"})

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            "form": UserCreationForm(),
            'title': "Registrarse"
        })
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"]
                )
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                messages.warning(request, 'Usuario ya existe.')
                return render(request, 'signup.html', {
                    "form": UserCreationForm(),
                    'title': "Registrarse"
                    #"error": "Usuario ya existe."
                })
        else:
            messages.warning(request, 'Contraseña no coincide.')
            return render(request, 'signup.html', {
                "form": UserCreationForm(),
                'title': "Registrarse"
                #"error": "Contraseña no coincide."
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
        if user is None:
            messages.warning(request, 'Usuario/Contraseña no valido.')
            return render(request, 'signin.html', {"form": LoginForm(),
            'title': "Inicia sesión"})

        login(request, user)
        return redirect('home')