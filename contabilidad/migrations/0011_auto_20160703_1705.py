# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('contabilidad', '0010_auto_20160210_2314'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consumidor',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Nombre_entrada',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_transaccion',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Transaccion',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('monto', models.IntegerField(max_length=30)),
                ('fecha', models.DateField()),
                ('descripcion', models.TextField(max_length=300)),
                ('consumidor', models.ForeignKey(to='contabilidad.Consumidor')),
                ('nombre_entrada', smart_selects.db_fields.ChainedForeignKey(chained_model_field='Tipo_transaccion', to='contabilidad.Nombre_entrada', chained_field='Tipo_transaccion', auto_choose=True)),
                ('tipo_transaccion', models.ForeignKey(to='contabilidad.Tipo_transaccion')),
            ],
        ),
        migrations.AddField(
            model_name='nombre_entrada',
            name='tipo_transaccion',
            field=models.ForeignKey(to='contabilidad.Tipo_transaccion'),
        ),
    ]
