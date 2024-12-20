from django.contrib import admin
from .models import Grupo

@admin.register(Grupo)
class GrupoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'codigoAcesso', 'emailAdmin', 'diasAtivos', 'criadoEm')
    search_fields = ('nome', 'codigoAcesso', 'emailAdmin')
