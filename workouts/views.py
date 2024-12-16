from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import TreinoForm, SeriesForm
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

@login_required
def adicionar_serie_view(request, treino_id):
    treino = get_object_or_404(Treino, id=treino_id, usuario=request.user)
    if request.method == 'POST':
        form = SeriesForm(request.POST)
        if form.is_valid():
            serie = form.save(commit=False)
            serie.treino = treino
            serie.save()
            return redirect('detalhar_treino', treino_id=treino.id)
    else:
        form = SeriesForm()
    return render(request, 'workouts/adicionar_serie.html', {'form': form, 'treino': treino})
  
@login_required
def detalhar_treino_view(request, treino_id):
    treino = get_object_or_404(Treino, id=treino_id, usuario=request.user)
    series = treino.series.all().order_by('ordemDoTreino')
    return render(request, 'workouts/detalhar_treino.html', {'treino': treino, 'series': series})
