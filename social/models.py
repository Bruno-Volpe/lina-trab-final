from django.db import models
from django.utils import timezone
from django.conf import settings
from groups.models import Grupo

class Post(models.Model):
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, related_name='posts')
    data = models.DateTimeField(default=timezone.now)
    titulo = models.CharField(max_length=255)
    urlDaImagem = models.URLField(max_length=500, null=True, blank=True)
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.titulo
