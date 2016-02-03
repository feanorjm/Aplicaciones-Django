# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contabilidad', '0007_monthlyweatherbycity'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MonthlyWeatherByCity',
        ),
    ]
