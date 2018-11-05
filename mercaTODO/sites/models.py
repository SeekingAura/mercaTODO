from django.db import models

# Validators
import re
from django.core.exceptions import ValidationError

def numeric_validator(value):
	result=re.match('[0-9]*', str(value))
	if result is not None:	
		if len(result.group(0))!=len(str(value)):
			raise ValidationError('este campo debe ser solamente númerico')
	else:
		raise ValidationError('este campo debe ser solamente númerico')

# Create your models here.
class Site(models.Model):
	name=models.CharField(max_length=500, verbose_name="Nombre")
	address=models.CharField(max_length=750, blank=True, null=True, default=None, verbose_name="Dirección")
	timeOpen=models.CharField(max_length=500, blank=True, null=True, default=None, verbose_name="Horario")
	phone=models.CharField(max_length=250, blank=True, null=True, default=None, verbose_name="Telefono")
	webSite=models.CharField(max_length=500, blank=True, null=True, default=None, verbose_name="Sitio Web")
	image=models.ImageField(upload_to="sites", blank=True, null=True, default=None, verbose_name="Imagen")

	def __str__(self):
		return self.name

	
