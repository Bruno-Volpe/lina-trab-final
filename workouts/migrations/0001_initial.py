# Generated by Django 5.1.4 on 2024-12-12 22:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('equipamento', models.CharField(blank=True, max_length=255, null=True)),
                ('tipo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Treino',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('dia', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Cardio',
            fields=[
                ('exercicio_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='workouts.exercicio')),
                ('duracao', models.IntegerField(help_text='Duração em minutos')),
            ],
            bases=('workouts.exercicio',),
        ),
        migrations.CreateModel(
            name='Musculacao',
            fields=[
                ('exercicio_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='workouts.exercicio')),
                ('grupoMuscular', models.CharField(max_length=100)),
            ],
            bases=('workouts.exercicio',),
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordemDoTreino', models.IntegerField()),
                ('numeroRepeticao', models.IntegerField()),
                ('carga', models.CharField(blank=True, max_length=50, null=True)),
                ('exercicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='series', to='workouts.exercicio')),
                ('treino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='series', to='workouts.treino')),
            ],
        ),
    ]
