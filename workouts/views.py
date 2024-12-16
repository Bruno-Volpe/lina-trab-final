from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import TreinoForm
from .models import Treino

@login_required
def criar_treino_view(request):
    if request.method == 'POST':
        form = TreinoForm(request.POST)
        if form.is_valid():
            treino = form.save(commit=False)
            treino.usuario = request.user
            treino.save()
            return redirect('listar_treinos')
    else:
        form = TreinoForm()
    return render(request, 'workouts/criar_treino.html', {'form': form})

@login_required
def listar_treinos_view(request):
    treinos = Treino.objects.filter(usuario=request.user)
    return render(request, 'workouts/listar_treinos.html', {'treinos': treinos})
