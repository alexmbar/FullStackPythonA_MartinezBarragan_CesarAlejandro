from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Personas


class SignupForm(UserCreationForm):
    username = forms.CharField(label="Usuario", widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Ingresa su usuario"}))   
    password1 = forms.CharField(label="password1", widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Ingresa su contraseña"})) 
    password2 = forms.CharField(label="password2", widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Ingresa su contraseña"})) 
    nombre = forms.CharField(label="Nombre", widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Ingresa su nombre"}))
    apellidos = forms.CharField(label="Apellidos", widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Ingresa su apellido"}))
    edad = forms.IntegerField(label="Edad", widget=forms.NumberInput(attrs={"class":"form-control","placeholder":"Ingresa su edad"}))
    calle = forms.CharField(label="Calle", widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Ingresa su calle"}))
    colonia = forms.CharField(label="Colonia", widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Ingresa su colonia"}))
    codigo_postal = forms.CharField(label="Código Postal", widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Ingresa su código postal"}))
    estado = forms.CharField(label="Estado", widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Ingresa su estado"}))

    class Meta:
        model = User
        fields = ['username', 'nombre', 'apellidos', 'edad', 'calle', 'colonia', 'codigo_postal', 'estado']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.save()
        
        nombre = self.cleaned_data['nombre']
        apellidos = self.cleaned_data['apellidos']
        edad = self.cleaned_data['edad']
        calle = self.cleaned_data['calle']
        colonia = self.cleaned_data['colonia']
        codigo_postal = self.cleaned_data['codigo_postal']
        estado = self.cleaned_data['estado']
        
        persona = Personas.objects.create(usuario=user, nombre=nombre, apellidos=apellidos, edad=edad, calle=calle, colonia=colonia, codigo_postal=codigo_postal, estado=estado)
        persona.save()

        return user