# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guiacontactos', '0004_personas_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personas',
            name='descripcion',
            field=models.TextField(null=True, max_length=300),
        ),
    ]
