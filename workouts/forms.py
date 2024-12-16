from django import forms
from .models import Treino

class TreinoForm(forms.ModelForm):
    class Meta:
        model = Treino
        fields = ['nome', 'dia']
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Nome do treino'}),
            'dia': forms.TextInput(attrs={'placeholder': 'Dia da semana'})
        }
