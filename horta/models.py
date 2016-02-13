from __future__ import unicode_literals
from django.db import models
import datetime

class Difficulty(models.Model):
    description = models.CharField(max_length=30)

class Weather(models.Model):
    description = models.CharField(max_length=30)

class Plant(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    min_temperature = models.IntegerField()
    max_temperature = models.IntegerField()
    min_days_cultivation = models.IntegerField()
    max_days_cultivation = models.IntegerField()
    difficulty = models.ForeignKey(Difficulty)
    weather = models.ForeignKey(Weather)
    created_at = models.DateTimeField('Criado em', default = datetime.datetime.now)
    updated_at = models.DateTimeField('Atualizado em', default = datetime.datetime.now) 