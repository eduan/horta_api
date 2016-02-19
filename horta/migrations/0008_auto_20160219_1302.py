# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('horta', '0007_auto_20160219_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='growing',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Criado em'),
        ),
        migrations.AlterField(
            model_name='growing',
            name='updated_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Atualizado em'),
        ),
        migrations.AlterField(
            model_name='growingstage',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Criado em'),
        ),
        migrations.AlterField(
            model_name='growingstage',
            name='updated_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Atualizado em'),
        ),
        migrations.AlterField(
            model_name='plant',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Criado em'),
        ),
        migrations.AlterField(
            model_name='plant',
            name='updated_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Atualizado em'),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Criado em'),
        ),
        migrations.AlterField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Atualizado em'),
        ),
    ]
