from django.db import models

class Exercicio(models.Model):
    nome = models.CharField(max_length=255)
    equipamento = models.CharField(max_length=255, null=True, blank=True)
    tipo = models.CharField(max_length=50)  # ex: 'musculacao' ou 'cardio'

    def __str__(self):
        return self.nome

class Treino(models.Model):
    nome = models.CharField(max_length=255)
    dia = models.CharField(max_length=50)  # Por ex: 'Segunda', 'Terça', etc.

    def __str__(self):
        return f"{self.nome} ({self.dia})"

class Series(models.Model):
    treino = models.ForeignKey(Treino, on_delete=models.CASCADE, related_name='series')
    ordemDoTreino = models.IntegerField()
    numeroRepeticao = models.IntegerField()
    carga = models.CharField(max_length=50, null=True, blank=True)
    exercicio = models.ForeignKey(Exercicio, on_delete=models.CASCADE, related_name='series')

    def __str__(self):
        return f"{self.exercicio.nome} - {self.numeroRepeticao} repetições"

class Musculacao(Exercicio):
    grupoMuscular = models.CharField(max_length=100)

class Cardio(Exercicio):
    duracao = models.IntegerField(help_text="Duração em minutos")
