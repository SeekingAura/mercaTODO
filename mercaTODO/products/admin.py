from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import *
# Register your models here.

typeUnitDict={
	'unit':'Unidad',
	'gram':'Gramo',
	'pound':'Libra',
	'kilogram':'Kilogramo',
}
class ProductSiteAdmin(ModelAdmin):
    search_fields = ('site', 'product')
    list_display = ('site', 'product', 'Unidad_de_venta','price')
    def Unidad_de_venta(self, obj):
        return typeUnitDict.get(obj.product.unit)
admin.site.register(Product)
admin.site.register(SiteProduct, ProductSiteAdmin)