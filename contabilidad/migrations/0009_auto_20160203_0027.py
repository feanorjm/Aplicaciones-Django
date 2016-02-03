# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contabilidad', '0008_delete_monthlyweatherbycity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transacciones',
            name='descripcion',
            field=models.TextField(max_length=300, blank=True),
        ),
        migrations.AlterField(
            model_name='transacciones',
            name='fecha',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='transacciones',
            name='tipo_gasto',
            field=models.CharField(choices=[('CASA', 'Casa'), ('COMBUSTIBLE', 'Combustible'), ('DEUDA_BANCARIA', 'Deuda bancaria'), ('DEUDA_GENERAL', 'Deuda General'), ('FAMILIAR', 'Familiar'), ('INZUMOS_OBRAS', 'Inzumos obras'), ('NO_ESPECIFICADO', 'No especificado'), ('PERSONAL', 'Personal'), ('SUELDOS', 'Sueldos'), ('TELEFONO', 'Telefono'), ('TRAMITESYOFICINA', 'Tramites y oficina')], default='CASA', blank=True, max_length=20),
        ),
    ]
