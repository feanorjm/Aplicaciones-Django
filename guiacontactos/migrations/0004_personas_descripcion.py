# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guiacontactos', '0003_auto_20151201_1921'),
    ]

    operations = [
        migrations.AddField(
            model_name='personas',
            name='descripcion',
            field=models.TextField(max_length=200, null=True),
        ),
    ]
