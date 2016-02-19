# -*- coding: utf-8 -*-
from django.test import TestCase

from horta.models import User, Plant, Growing, ConditionType, Condition, ConditionInterval, GrowingStage
from horta.services import startGrowing

class GrowingTestCase(TestCase):
    def setUp(self):
        ph = ConditionType.objects.create(name='Ph')
        temperatura = ConditionType.objects.create(name='Temperatura')
        dias = ConditionType.objects.create(name='Dias')
        clima = ConditionType.objects.create(name='Clima')
        luminosidade = ConditionType.objects.create(name='Luminosidade')
        irrigacao = ConditionType.objects.create(name='Irrigação')
        germinacao = ConditionType.objects.create(name='Germinação')

        Condition.objects.create(condition_type=irrigacao,description='Sempre Úmido')
        Condition.objects.create(condition_type=irrigacao, description='Levemente Úmido')
        Condition.objects.create(condition_type=luminosidade, description='Sombra')
        Condition.objects.create(condition_type=luminosidade, description='Luz Solar Direta')
        Condition.objects.create(condition_type=clima, description='Semiárido')
        Condition.objects.create(condition_type=clima, description='Subtropical')
        Condition.objects.create(condition_type=clima, description='Tropical')
        ConditionInterval.objects.create(condition_type=germinacao,min=3,max=5)
        ConditionInterval.objects.create(condition_type=ph,min=6,max=7)
        ConditionInterval.objects.create(condition_type=dias,min=55,max=130)
        ConditionInterval.objects.create(condition_type=temperatura,min=10,max=24)

        User.objects.create(email='email@teste.com', phonenumber='1239823923', password='ah#$1234#4$')
        User.objects.create(email='email2@teste2.com', phonenumber='1198287398', password='kj@3jk#j4#*8')

        plant = Plant.objects.create(
            name='Planta teste',
            description='Planta teste nome em latim alguma coisa sei la',
            temperature=ConditionInterval.objects.get(pk=1),
            days=ConditionInterval.objects.get(pk=2),
            ph=ConditionInterval.objects.get(pk=3),
            depth=1)
        GrowingStage.objects.create(
            description='Plantio',
            days = 1,
            step = 1,
            plant = plant
        )
        GrowingStage.objects.create(
            description='Germinação',
            days = 5,
            step = 2,
            plant = plant
        )
        # condition=Condition.objects.get(pk=1),
    def testCreatingGrowning(self):
        plant = Plant.objects.get(pk=1)
        user = User.objects.get(email='email@teste.com')
        startGrowing(user,plant)
        g = Growing.objects.get(user_email='email@teste.com')
        self.assertTrue(g.pk > 0)

