from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.template import loader

from django.contrib.auth.decorators import login_required

from sites.models import Site
from products.models import SiteProduct

@login_required(login_url='domain:login')
def misProductos(request):
	ctx={"productos":{}}
	user_id = request.user
	try:
		sitio=Site.objects.get(User_id=user_id)#verify is a site
	except:
		return redirect("domain:index")


	if(request.method == "POST"):
		value_btn = request.POST.get('btn_value')
		if (value_btn == "deleteProducto"):
			producto_id = request.POST.get('producto')
			producto=SiteProduct.objects.get(site=sitio, product_id=producto_id)
			producto.delete()




	productos= SiteProduct.objects.filter(site=sitio)
	ctx["productos"]=productos
	template = loader.get_template('sites/control.html')
	
	return HttpResponse(template.render(ctx, request))