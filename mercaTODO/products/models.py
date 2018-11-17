from django.db import models
from sites.models import Site
# from django.contrib.auth.models import User



# other data
typeUnit=(
	('Unidad', 'Unidad'),
	('Gramo','Gramo'),
	('Libra','Libra'),
	('Kilogramo' ,'Kilogramo'),
	)

statusChoices=(
	('Sin cambios', 'Sin cambios'),
	('Nuevo','Nuevo'),
	('Modificado','Modificado'),
	)

# Create your models here.
class Product(models.Model):
	name = models.CharField(max_length=500, verbose_name="Nombre")
	unit = models.CharField(choices=typeUnit, default='Unidad', max_length=20, verbose_name="Unidad de venta")
	image=models.ImageField(upload_to="products", blank=True, null=True, default=None, verbose_name="Imagen")
	def __str__(self):
		return self.name



class SiteProduct(models.Model):
	site=models.ForeignKey(Site, on_delete=models.CASCADE, verbose_name="Sitio de Venta")
	product=models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Producto")
	price = models.FloatField(default=0.0, verbose_name="Precio por Unidad de venta")
	newPrice = models.FloatField(default=0.0, verbose_name="Precio nuevo al modificar")
	status = models.CharField(choices=statusChoices, max_length=20, verbose_name="Estado de almacenamiento", default="Sin cambios")
	lastUpdate=models.DateTimeField(auto_now=True)
	def __str__(self):
		return str(self.site)+" "+str(self.product)
