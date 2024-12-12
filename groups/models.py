from django.db import models
from django.utils import timezone
from django.conf import settings

class Grupo(models.Model):
    codigoAcesso = models.CharField(max_length=50, unique=True)
    nome = models.CharField(max_length=255)
    criadoEm = models.DateTimeField(default=timezone.now)
    emailAdmin = models.EmailField()
    diasAtivos = models.IntegerField(default=0)
    membros = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)  # Relacionamento com Usuários

    def __str__(self):
        return self.nome
