from django.urls import path
from .views import criar_treino_view, listar_treinos_view

urlpatterns = [
    path('criar/', criar_treino_view, name='criar_treino'),
    path('', listar_treinos_view, name='listar_treinos'),
]
