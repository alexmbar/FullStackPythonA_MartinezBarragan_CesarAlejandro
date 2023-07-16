from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Personas, Reportes
from .choices import ESTADOS_CHOICES

class SignupForm(UserCreationForm):
    username = forms.CharField(label="Usuario", widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Ingresa su usuario"}))   
    password1 = forms.CharField(label="password1", widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Ingresa su contraseña"})) 
    password2 = forms.CharField(label="password2", widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Ingresa su contraseña"})) 
    nombre = forms.CharField(label="Nombre", widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Ingresa su nombre"}))
    apellidos = forms.CharField(label="Apellidos", widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Ingresa su apellido"}))
    edad = forms.IntegerField(label="Edad", widget=forms.NumberInput(attrs={"class":"form-control","placeholder":"Ingresa su edad"}))
    calle = forms.CharField(label="Calle", widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Ingresa su calle"}))
    numero = forms.IntegerField(label="Numero",widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Ingresa su número"}))
    colonia = forms.CharField(label="Colonia", widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Ingresa su colonia"}))
    codigo_postal = forms.IntegerField(label="Código Postal", widget=forms.NumberInput(attrs={"class":"form-control","placeholder":"Ingresa su código postal"}))
    estado = forms.ChoiceField(label="Estado", choices = ESTADOS_CHOICES, widget=forms.Select(attrs={"class":"form-control"}))
    email = forms.CharField(label="eMail", widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Ingresa su email"}))
    ciudad = forms.CharField(label="Ciudad", widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Ingresa su ciudad"}))

    class Meta:
        model = User
        fields = ['username', 'nombre', 'apellidos', 'edad', 'calle', 'colonia', 'codigo_postal', 'estado', 'ciudad']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.save()
        
        nombre = self.cleaned_data['nombre']
        apellidos = self.cleaned_data['apellidos']
        edad = self.cleaned_data['edad']
        calle = self.cleaned_data['calle']
        numero = self.cleaned_data['numero']
        colonia = self.cleaned_data['colonia']
        codigo_postal = self.cleaned_data['codigo_postal']
        estado = self.cleaned_data['estado']
        ciudad = self.cleaned_data['ciudad']
        email = self.cleaned_data['email']
        
        persona = Personas.objects.create(usuario=user, nombre=nombre, apellidos=apellidos, edad=edad, calle=calle, numero=numero, colonia=colonia, codigo_postal=codigo_postal, estado=estado, ciudad=ciudad, email=email)
        persona.save()

        return user

class ReportForm(forms.ModelForm):
    descripcion = forms.CharField(label="Descripción", widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Ingresa la descripción"}))
    calle = forms.CharField(label="Calle", widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Ingresa su calle"}))
    numero = forms.IntegerField(label="Numero",widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Ingresa su número"}))
    colonia = forms.CharField(label="Colonia", widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Ingresa su colonia"}))
    codigo_postal = forms.IntegerField(label="Código Postal", widget=forms.NumberInput(attrs={"class":"form-control","placeholder":"Ingresa su código postal"}))
    estado = forms.ChoiceField(label="Estado", choices=ESTADOS_CHOICES, widget=forms.Select(attrs={"class":"form-control"}))
    ciudad = forms.CharField(label="Ciudad", widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Ingresa su ciudad"}))
    tipo_reporte = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = Reportes
        fields = ['descripcion', 'calle', 'numero','colonia', 'codigo_postal', 'estado','ciudad','tipo_reporte']

    def save(self, commit=True):
        reporte = super().save(commit=False)
        reporte.save()
        
        return reporte

class LoginForm(forms.Form):
    username = forms.CharField(label="Usuario", widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Ingresa su usuario"}))   
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Ingresa su contraseña"})) 
    
class PersonasForm(forms.ModelForm):
    class Meta:
        model = Personas
        fields = ['nombre', 'apellidos', 'edad', 'calle', 'numero', 'colonia', 'ciudad', 'email', 'codigo_postal', 'estado']
