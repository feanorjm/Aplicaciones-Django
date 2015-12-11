# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guiacontactos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='personas',
            name='apellido',
            field=models.CharField(null=True, max_length=40),
        ),
        migrations.AddField(
            model_name='personas',
            name='direccion',
            field=models.CharField(null=True, max_length=60),
        ),
        migrations.AddField(
            model_name='personas',
            name='oficio',
            field=models.CharField(null=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='personas',
            name='email',
            field=models.EmailField(null=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='personas',
            name='nombre',
            field=models.CharField(null=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='personas',
            name='telefono',
            field=models.CharField(null=True, max_length=20),
        ),
    ]
