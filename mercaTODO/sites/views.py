from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.template import loader

from django.db.models.query import QuerySet

from django.contrib.auth.decorators import login_required
# Models
from sites.models import Site
from products.models import SiteProduct, Product

#Others
from datetime import datetime

@login_required(login_url='domain:login')
def misProductos(request):
	error=[False, ""]
	ctx={"productos":None, "nuevos":False, "modificados":False, "error":error, "dataModificados":False}
	user_id = request.user
	try:
		sitio=Site.objects.get(User_id=user_id)#verify is a site
	except:
		return redirect("domain:index")

	
	if(request.method == "POST"):
		value_btn = request.POST.get('btn_value')
		if(value_btn == "addProducto"):
			nuevosProductos=SiteProduct.objects.filter(site=sitio, status="Nuevo")
			nuevosProductos.update(status="Sin cambios")
		if(value_btn == "addProductoCancel"):
			nuevosProductos=SiteProduct.objects.filter(site=sitio, status="Nuevo")
			nuevosProductos.delete()
		
		if(value_btn == "modProducto"):
			modificadosProductos=SiteProduct.objects.filter(site=sitio, status="Modificado")
			for modificadoProducto in modificadosProductos:
				modificadoProducto.price=modificadoProducto.newPrice
				modificadoProducto.status="Sin cambios"
				modificadoProducto.save()
		if(value_btn == "modProductoCancel"):
			nuevosProductos=SiteProduct.objects.filter(site=sitio, status="Modificado")
			nuevosProductos.update(status="Sin cambios")
		
		
		
		if (value_btn == "deleteProducto"):
			producto_id = request.POST.get('producto')
			producto=SiteProduct.objects.get(site=sitio, product_id=producto_id)
			producto.delete()

		if(value_btn == "fileAdd"):
			try:
				operations=request.FILES['fileProducts'].read().decode("utf-8").split("\n")
				for enum, operation in enumerate(operations):
					data=operation.split("| ")
					if(len(data)<2 or len(data)>3):
						error[0]=True
						error[1]="Fallo en el formato, cantidad de argumentos invalida, linea #{}".format(enum)
						break
					try:
						nameProduct=data[0]
						priceProduct=float(data[1])
					except:
						error[0]=True
						error[1]="Fallo en el formato, algo está mal escrito en la linea #{}".format(enum)
						break
					try:
						producto=Product.objects.get(name=nameProduct)
					except:
						error[0]=True
						error[1]+="El producto {}, no está en el sistema, verifique que esté bien escrito o en su defecto solicite crearlo de la linea #{} \n".format(nameProduct, enum)
						continue
					try:
						try:
							sitioProducto=SiteProduct.objects.get(site=sitio, product=producto)
							if(sitioProducto.status=="Nuevo"):
								continue
							sitioProducto.newPrice=priceProduct
							sitioProducto.status="Modificado"
							sitioProducto.save()
						except:
							SiteProduct.objects.create(site=sitio, product=producto, price=priceProduct, status="Nuevo")
								
								#productos.intersection(mergeData)

					except:
						error[0]=True
						error[1]+="El producto {}, ha generado un problema linea #{} \n".format(nameProduct, enum)
						continue
			except:
				error[0]=True
				error[1]="Fallo al abrir el archivo"
			
	productos= SiteProduct.objects.filter(site=sitio)
	productosNuevos=SiteProduct.objects.filter(status="Nuevo")
	if(len(productosNuevos)>0):
		ctx["nuevos"]=True	
	productosModificados=SiteProduct.objects.filter(status="Modificado")
	if(len(productosModificados)>0):
		ctx["modificados"]=True

	
	ctx["productos"]=productos
	template = loader.get_template('sites/control.html')
	
	return HttpResponse(template.render(ctx, request))