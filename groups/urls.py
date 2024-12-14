from django.urls import path
from .views import criar_grupo_view, listar_grupos_view

urlpatterns = [
    path('criar/', criar_grupo_view, name='criar_grupo'),
    path('', listar_grupos_view, name='listar_grupos'),
]
