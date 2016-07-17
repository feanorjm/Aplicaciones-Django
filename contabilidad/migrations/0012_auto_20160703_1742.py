# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('contabilidad', '0011_auto_20160703_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaccion',
            name='nombre_entrada',
            field=smart_selects.db_fields.ChainedForeignKey(to='contabilidad.Nombre_entrada'),
        ),
    ]
