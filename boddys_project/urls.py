from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),          # Página inicial
    path('users/', include('users.urls')),    # Autenticação
    path('groups/', include('groups.urls')),  # Grupos
    path('workouts/', include('workouts.urls')), # Treinos
    path('social/', include('social.urls')), # Posts
]
