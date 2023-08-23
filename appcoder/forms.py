from django import forms

class oficinasform(forms.Form)
    nombre=forms.CharField(max_length=50)
    ubicacion=forms.CharField(max_length=50)


class personalform(forms.Form)
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    email=forms.EmailField()
    telefono=forms.IntegerField()
    