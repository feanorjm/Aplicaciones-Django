from django.db import models

class Transacciones(models.Model):

	NOMBRE_CONSUMIDOR = (
		('FRANCISCO', 'Francisco'),
		('ALEXIS', 'Alexis'),
        ('DEPARTAMENTO', 'Departamento'),
        ('EMPRESA', 'Empresa'),
        ('FAMILIA', 'Familia'),
        ('OBRAS', 'Obras'),
        ('CAMILO', 'Camilo'),
        ('JUAN', 'Juan'),
        )

	TIPO_GASTOS = (
    	('CASA', 'Casa'),
    	('COMBUSTIBLE', 'Combustible'),
    	('DEUDA_BANCARIA', 'Deuda bancaria'),
    	('DEUDA_GENERAL', 'Deuda General'),
    	('FAMILIAR', 'Familiar'),
    	('INZUMOS_OBRAS', 'Inzumos obras'),
    	('NO_ESPECIFICADO', 'No especificado'),
    	('PERSONAL', 'Personal'),
    	('SUELDOS', 'Sueldos'),
    	('TELEFONO', 'Telefono'),
    	('TRAMITESYOFICINA', 'Tramites y oficina'),
    	)

	consumidor = models.CharField(max_length=15, choices=NOMBRE_CONSUMIDOR, default='FRANCISCO')
	monto = models.IntegerField(max_length=30)
	tipo_gasto = models.CharField(max_length=20, choices=TIPO_GASTOS, default='CASA', blank=True)
	fecha = models.DateField(auto_now=False, auto_now_add=False, blank=True)
	descripcion = models.TextField(max_length=300, blank=True)

	def __str__(self):
		return self.descripcion




