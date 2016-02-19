# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('horta', '0006_auto_20160219_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='growing',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 19, 13, 1, 46, 446966, tzinfo=utc), verbose_name='Criado em'),
        ),
        migrations.AlterField(
            model_name='growing',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 19, 13, 1, 46, 446989, tzinfo=utc), verbose_name='Atualizado em'),
        ),
        migrations.AlterField(
            model_name='growingstage',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 19, 13, 1, 46, 446156, tzinfo=utc), verbose_name='Criado em'),
        ),
        migrations.AlterField(
            model_name='growingstage',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 19, 13, 1, 46, 446179, tzinfo=utc), verbose_name='Atualizado em'),
        ),
        migrations.AlterField(
            model_name='plant',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 19, 13, 1, 46, 444319, tzinfo=utc), verbose_name='Criado em'),
        ),
        migrations.AlterField(
            model_name='plant',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 19, 13, 1, 46, 444345, tzinfo=utc), verbose_name='Atualizado em'),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 19, 13, 1, 46, 445611, tzinfo=utc), verbose_name='Criado em'),
        ),
        migrations.AlterField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 19, 13, 1, 46, 445634, tzinfo=utc), verbose_name='Atualizado em'),
        ),
    ]
