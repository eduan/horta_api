# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-12 00:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clima',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Dificuldade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Planta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('min_temperatura', models.IntegerField()),
                ('max_temperatura', models.IntegerField()),
                ('min_dias_cultivo', models.IntegerField()),
                ('max_dias_cultivo', models.IntegerField()),
                ('created_at', models.DateTimeField(default=datetime.datetime.now, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(default=datetime.datetime.now, verbose_name='Atualizado em')),
                ('clima', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='horta.Clima')),
                ('dificuldade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='horta.Dificuldade')),
            ],
        ),
    ]