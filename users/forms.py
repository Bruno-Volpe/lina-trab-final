from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class SignUpForm(UserCreationForm):
    nome = forms.CharField(max_length=255, required=True)
    dataNascimento = forms.DateField(required=False, widget=forms.DateInput(attrs={'type':'date'}))
    urlFotoPerfil = forms.URLField(required=False)

    class Meta:
        model = Usuario
        fields = ['email', 'nome', 'dataNascimento', 'urlFotoPerfil', 'password1', 'password2']
