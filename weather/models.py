from django.db import models


class Weather(models.Model):
    temperature = models.IntegerField(default=0)
    wind = models.IntegerField(default=0)
    humidity = models.IntegerField(default=0)
    condition = models.CharField(max_length=50)
