# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guiacontactos', '0002_auto_20151201_0135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personas',
            name='email',
            field=models.EmailField(blank=True, null=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='personas',
            name='oficio',
            field=models.CharField(null=True, max_length=40),
        ),
    ]
