# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transacciones',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('consumidor', models.CharField(max_length=15, choices=[('FRANCISCO', 'Francisco'), ('ALEXIS', 'Alexis'), ('DEPARTAMENTO', 'Departamento'), ('EMPRESA', 'Empresa'), ('FAMILIA', 'Familia'), ('OBRAS', 'Obras'), ('CAMILO', 'Camilo'), ('JUAN', 'Juan')])),
                ('monto', models.IntegerField()),
                ('fecha', models.DateField()),
                ('descripcion', models.TextField(max_length=300)),
            ],
        ),
    ]
