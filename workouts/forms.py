from django import forms
from .models import Treino, Series


class TreinoForm(forms.ModelForm):
    class Meta:
        model = Treino
        fields = ['nome', 'dia']
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Nome do treino'}),
            'dia': forms.TextInput(attrs={'placeholder': 'Dia da semana'})
        }


class SeriesForm(forms.ModelForm):
    class Meta:
        model = Series
        fields = ['exercicio', 'ordemDoTreino', 'numeroRepeticao', 'carga']
        labels = {
            'exercicio': 'Exercício',
            'ordemDoTreino': 'Ordem no Treino',
            'numeroRepeticao': 'Número de Repetições',
            'carga': 'Carga/Intensidade'
        }
        widgets = {
            'ordemDoTreino': forms.NumberInput(attrs={'min': 1}),
            'numeroRepeticao': forms.NumberInput(attrs={'min': 1}),
            'carga': forms.TextInput(attrs={'placeholder': 'Ex: 20kg, 50m, etc.'}),
        }