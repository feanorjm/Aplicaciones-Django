# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contabilidad', '0004_auto_20160113_2150'),
    ]

    operations = [
        migrations.CreateModel(
            name='MonthlyWeatherByCity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('month', models.IntegerField()),
                ('boston_temp', models.DecimalField(decimal_places=1, max_digits=5)),
                ('houston_temp', models.DecimalField(decimal_places=1, max_digits=5)),
            ],
        ),
    ]
