from django import forms
from groups.models import Grupo
from .models import Post

class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(PostForm, self).__init__(*args, **kwargs)
        if user:
            # Filtra os grupos que o usuário participa
            self.fields['grupo'].queryset = Grupo.objects.filter(membros=user)

    class Meta:
        model = Post
        fields = ['grupo', 'titulo', 'urlDaImagem']
        labels = {
            'grupo': 'Grupo',
            'titulo': 'Título do Post',
            'urlDaImagem': 'URL da Imagem (opcional)'
        }
        widgets = {
            'titulo': forms.TextInput(attrs={'placeholder': 'Digite o título do post'}),
            'urlDaImagem': forms.URLInput(attrs={'placeholder': 'Cole a URL da imagem, se desejar'})
        }
