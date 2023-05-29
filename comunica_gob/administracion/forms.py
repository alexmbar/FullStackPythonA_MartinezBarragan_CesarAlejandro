from dataclasses import field
from socket import fromshare
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="Usuario", widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Ingresa su usuario"}))
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Ingresa su contraseña"}))
