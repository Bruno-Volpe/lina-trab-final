# accounts/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from .models import Usuario

User = get_user_model()

class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'placeholder': 'exemplo@exemplo.com',
            'class': 'form-control'
        }),
        label='Email',
        error_messages={
            'required': 'Por favor, insira seu endereço de email.',
            'invalid': 'Digite um endereço de email válido.'
        }
    )
    nome = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Seu Nome Completo',
            'class': 'form-control'
        }),
        label='Nome Completo',
        error_messages={
            'required': 'Por favor, insira seu nome completo.',
            'max_length': 'O nome não pode exceder 255 caracteres.'
        }
    )
    dataNascimento = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control'
        }),
        label='Data de Nascimento',
        error_messages={
            'invalid': 'Digite uma data válida.'
        }
    )
    urlFotoPerfil = forms.URLField(
        required=False,
        widget=forms.URLInput(attrs={
            'placeholder': 'https://seuwebsite.com/foto.jpg',
            'class': 'form-control'
        }),
        label='URL da Foto de Perfil',
        error_messages={
            'invalid': 'Digite uma URL válida.'
        }
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': '******',
            'class': 'form-control'
        }),
        label='Senha',
        error_messages={
            'required': 'Por favor, insira sua senha.'
        }
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': '******',
            'class': 'form-control'
        }),
        label='Confirme sua Senha',
        error_messages={
            'required': 'Por favor, confirme sua senha.'
        }
    )

    class Meta:
        model = User
        fields = ['email', 'nome', 'dataNascimento', 'urlFotoPerfil', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este email já está em uso.')
        return email

    def clean_nome(self):
        nome = self.cleaned_data.get('nome')
        if not nome.replace(' ', '').isalpha():
            raise forms.ValidationError('O nome deve conter apenas letras e espaços.')
        return nome

class LoginForm(AuthenticationForm):
    username = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'placeholder': 'exemplo@exemplo.com',
            'class': 'form-control'
        }),
        label='Email',
        error_messages={
            'required': 'Por favor, insira seu endereço de email.',
            'invalid': 'Digite um endereço de email válido.'
        }
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': '******',
            'class': 'form-control'
        }),
        label='Senha',
        error_messages={
            'required': 'Por favor, insira sua senha.'
        }
    )

    class Meta:
        model = User
        fields = ['username', 'password']
