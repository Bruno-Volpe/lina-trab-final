from django import forms
from .models import Grupo

class GrupoForm(forms.ModelForm):
    class Meta:
        model = Grupo
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Nome do grupo'}),
        }
        
        
class GrupoJoinForm(forms.Form):
    codigo = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': 'Código de acesso'})
    )
