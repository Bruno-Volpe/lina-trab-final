from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import GrupoForm, GrupoJoinForm
from .models import Grupo
from django.contrib.auth import get_user_model
import random

User = get_user_model()

@login_required
def criar_grupo_view(request):
    if request.method == 'POST':
        form = GrupoForm(request.POST)
        if form.is_valid():    
            grupo = form.save(commit=False)
            grupo.codigoAcesso = random.randint(1000, 9999)
            # verifiy if the code is unique
            while Grupo.objects.filter(codigoAcesso=grupo.codigoAcesso).exists():
                grupo.codigoAcesso = random.randint(1000, 9999)
            grupo.emailAdmin = request.user.email
            grupo.save()
            # Adiciona o criador como membro do grupo
            grupo.membros.add(request.user)
            return redirect('listar_grupos')
    else:
        form = GrupoForm()
    return render(request, 'groups/criar_grupo.html', {'form': form})

@login_required
def listar_grupos_view(request):
    grupos = Grupo.objects.filter(membros=request.user)
    return render(request, 'groups/listar_grupos.html', {'grupos': grupos})

@login_required
def join_grupo_view(request):
    if request.method == 'POST':
        form = GrupoJoinForm(request.POST)
        if form.is_valid():
            codigo = form.cleaned_data['codigo']
            try:
                grupo = Grupo.objects.get(codigoAcesso=codigo)
                if request.user in grupo.membros.all():
                    return render(request, 'groups/join_grupo.html', {
                        'form': form,
                        'error': 'Você já está no grupo'
                    })
                grupo.membros.add(request.user)
                return redirect('listar_grupos')
            except Grupo.DoesNotExist:
                return render(request, 'groups/join_grupo.html', {
                    'form': form,
                    'error': 'Código inválido'
                })
        else:
            # Formulário inválido
            return render(request, 'groups/join_grupo.html', {'form': form})
    else:
        form = GrupoJoinForm()
    return render(request, 'groups/join_grupo.html', {'form': form})
