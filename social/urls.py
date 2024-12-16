from django.urls import path
from .views import criar_post_view, listar_posts_grupo_view

urlpatterns = [
    path('criar/', criar_post_view, name='criar_post'),
    path('grupo/<int:grupo_id>/posts/', listar_posts_grupo_view, name='listar_posts_grupo'),
]
