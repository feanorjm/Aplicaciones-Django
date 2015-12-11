from django.db import models

class Personas(models.Model):
	nombre = models.CharField(max_length=40,null=True)
	apellido = models.CharField(max_length=40,null=True)
	telefono = models.CharField(max_length=20,null=True)
	direccion = models.CharField(max_length=60,null=True)
	email = models.EmailField(null=True, blank= True)
	oficio = models.CharField(max_length=40,null=True)
	descripcion = models.TextField(max_length=300,null=True)

	def __str__(self):
		return self.nombre