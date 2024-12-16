from django.urls import path
from .views import criar_treino_view, listar_treinos_view, detalhar_treino_view, adicionar_serie_view

urlpatterns = [
    path('criar/', criar_treino_view, name='criar_treino'),
    path('', listar_treinos_view, name='listar_treinos'),
    path('<int:treino_id>/', detalhar_treino_view, name='detalhar_treino'),
    path('<int:treino_id>/adicionar-serie/', adicionar_serie_view, name='adicionar_serie'),
]
