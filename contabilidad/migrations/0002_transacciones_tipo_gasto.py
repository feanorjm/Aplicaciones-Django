# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contabilidad', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transacciones',
            name='tipo_gasto',
            field=models.CharField(default='CASA', max_length=20, choices=[('CASA', 'Casa'), ('COMBUSTIBLE', 'Combustible'), ('DEUDA_BANCARIA', 'Deuda bancaria'), ('DEUDA_GENERAL', 'Deuda General'), ('FAMILIAR', 'Familiar'), ('INZUMOS_OBRAS', 'Inzumos obras'), ('NO_ESPECIFICADO', 'No especificado'), ('PERSONAL', 'Personal'), ('SUELDOS', 'Sueldos'), ('TELEFONO', 'Telefono'), ('TRAMITESYOFICINA', 'Tramites y oficina')]),
        ),
    ]
