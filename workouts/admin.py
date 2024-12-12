from django.contrib import admin
from .models import Exercicio, Treino, Series, Musculacao, Cardio

@admin.register(Exercicio)
class ExercicioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'equipamento', 'tipo')
    search_fields = ('nome', 'tipo')

@admin.register(Treino)
class TreinoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'dia')
    search_fields = ('nome', 'dia')

@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    list_display = ('treino', 'exercicio', 'ordemDoTreino', 'numeroRepeticao', 'carga')
    search_fields = ('exercicio__nome', 'treino__nome')

@admin.register(Musculacao)
class MusculacaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'grupoMuscular', 'equipamento', 'tipo')

@admin.register(Cardio)
class CardioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'duracao', 'equipamento', 'tipo')
