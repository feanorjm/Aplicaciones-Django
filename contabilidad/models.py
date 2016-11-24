from django.db import models
from smart_selects.db_fields import ChainedForeignKey


class Consumidor(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Tipo_transaccion(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Nombre_entrada(models.Model):
    tipo_transaccion = models.ForeignKey(Tipo_transaccion)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Transaccion(models.Model):
    tipo_transaccion = models.ForeignKey(Tipo_transaccion, default=1)
    consumidor = models.ForeignKey(Consumidor, default=1)
    monto = models.IntegerField()
    nombre_entrada = ChainedForeignKey(Nombre_entrada,chained_field="tipo_transaccion", chained_model_field="tipo_transaccion")
    fecha = models.DateField(auto_now=False, auto_now_add=False)
    descripcion = models.TextField(max_length=300)

    def __str__(self):
        return self.descripcion
