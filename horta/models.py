from __future__ import unicode_literals
from django.db import models
import datetime

class Dificuldade(models.Model):
    descricao = models.CharField(max_length=30)

class Clima(models.Model):
    descricao = models.CharField(max_length=30)

class Planta(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    min_temperatura = models.IntegerField()
    max_temperatura = models.IntegerField()
    min_dias_cultivo = models.IntegerField()
    max_dias_cultivo = models.IntegerField()
    dificuldade = models.ForeignKey(Dificuldade)
    clima = models.ForeignKey(Clima)
    created_at = models.DateTimeField('Criado em', default = datetime.datetime.now)
    updated_at = models.DateTimeField('Atualizado em', default = datetime.datetime.now) 