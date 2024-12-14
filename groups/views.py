from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import GrupoForm
from .models import Grupo
from django.contrib.auth import get_user_model

User = get_user_model()

@login_required
def criar_grupo_view(request):
    if request.method == 'POST':
        form = GrupoForm(request.POST)
        if form.is_valid():
            grupo = form.save(commit=False)
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
