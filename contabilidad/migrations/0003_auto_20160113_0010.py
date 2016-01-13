# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contabilidad', '0002_transacciones_tipo_gasto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transacciones',
            name='monto',
            field=models.IntegerField(max_length=30),
        ),
    ]
