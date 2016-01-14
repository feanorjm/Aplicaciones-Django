# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contabilidad', '0003_auto_20160113_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transacciones',
            name='consumidor',
            field=models.CharField(default='FRANCISCO', max_length=15, choices=[('FRANCISCO', 'Francisco'), ('ALEXIS', 'Alexis'), ('DEPARTAMENTO', 'Departamento'), ('EMPRESA', 'Empresa'), ('FAMILIA', 'Familia'), ('OBRAS', 'Obras'), ('CAMILO', 'Camilo'), ('JUAN', 'Juan')]),
        ),
    ]
