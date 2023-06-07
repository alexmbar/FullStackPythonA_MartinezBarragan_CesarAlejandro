from dataclasses import field
from socket import fromshare
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="Usuario", widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Ingresa su usuario"}))
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Ingresa su contraseña"}))

class SignupForm(forms.Form):
    username = forms.CharField(label="Usuario", widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Ingresa su usuario"}))
    name = forms.CharField(label="Nombre", widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Ingresa su nombre"}))
    lastname = forms.CharField(label="Apellidos", widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Ingresa su apellido"}))
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Ingresa su contraseña"}))
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Ingresa su contraseña"}))