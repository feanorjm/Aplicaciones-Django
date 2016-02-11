# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contabilidad', '0009_auto_20160203_0027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transacciones',
            name='descripcion',
            field=models.TextField(max_length=300),
        ),
        migrations.AlterField(
            model_name='transacciones',
            name='fecha',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='transacciones',
            name='tipo_gasto',
            field=models.CharField(default='CASA', max_length=20, choices=[('CASA', 'Casa'), ('COMBUSTIBLE', 'Combustible'), ('DEUDA_BANCARIA', 'Deuda bancaria'), ('DEUDA_GENERAL', 'Deuda General'), ('FAMILIAR', 'Familiar'), ('INZUMOS_OBRAS', 'Inzumos obras'), ('NO_ESPECIFICADO', 'No especificado'), ('PERSONAL', 'Personal'), ('SUELDOS', 'Sueldos'), ('TELEFONO', 'Telefono'), ('TRAMITESYOFICINA', 'Tramites y oficina')]),
        ),
    ]
