# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contabilidad', '0006_delete_monthlyweatherbycity'),
    ]

    operations = [
        migrations.CreateModel(
            name='MonthlyWeatherByCity',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('month', models.IntegerField()),
                ('boston_temp', models.DecimalField(max_digits=5, decimal_places=1)),
                ('houston_temp', models.DecimalField(max_digits=5, decimal_places=1)),
            ],
        ),
    ]
