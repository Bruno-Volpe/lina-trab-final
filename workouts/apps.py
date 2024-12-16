from django.apps import AppConfig

class WorkoutsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'workouts'

    def ready(self):
        # Import dentro do ready para evitar problemas de import circular
        from workouts.models import Exercicio
        # Cria ou obtém os exercícios padrão
        Exercicio.objects.get_or_create(
            nome="Supino Reto",
            equipamento="Barra",
            tipo="musculacao"
        )
        Exercicio.objects.get_or_create(
            nome="Agachamento Livre",
            equipamento="Barra",
            tipo="musculacao"
        )
        Exercicio.objects.get_or_create(
            nome="Corrida na Esteira",
            equipamento="Esteira",
            tipo="cardio"
        )
