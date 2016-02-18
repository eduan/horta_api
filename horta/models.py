from __future__ import unicode_literals
from django.db import models
import datetime

#Weather, Difficulty, Light
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class ConditionType(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Condition(models.Model):
    description = models.CharField(max_length=30)
    condition_type = models.ForeignKey(ConditionType)
    def  __str__(self):
        return self.condition_type.name + ': ' + self.description

@python_2_unicode_compatible
class ConditionInterval(models.Model):
    min = models.IntegerField(default=0)
    max = models.IntegerField(default=0)
    condition_type = models.ForeignKey(ConditionType)
    def  __str__(self):
        return self.condition_type.name + ' min: ' + str(self.min) + ' max: ' + str(self.max)

class Plant(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    condition = models.ManyToManyField(Condition, related_name='%(class)s_condition')
    temperature = models.ForeignKey(ConditionInterval, related_name='%(class)s_temp', default='', limit_choices_to={'condition_type_id': 3});
    days = models.ForeignKey(ConditionInterval, related_name='%(class)s_days', default='', limit_choices_to={'condition_type_id': 4});
    ph = models.ForeignKey(ConditionInterval, related_name='%(class)s_ph', default='', limit_choices_to={'condition_type_id': 2});
    depth = models.IntegerField(default=0)
    created_at = models.DateTimeField('Criado em', default = datetime.datetime.now)
    updated_at = models.DateTimeField('Atualizado em', default = datetime.datetime.now)
    def  __str__(self):
        return self.name

class Growing(models.Model):
    plant = models.ForeignKey(Plant)
