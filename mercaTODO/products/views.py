from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from sites.models import Site

#import datetime
#datetime.now() 

def ListProducts(request):
	ctx={"usuario":""}
	if (request.user.is_authenticated):
		user_id = request.user
		try:
			Site.objects.get(User_id=user_id)
			ctx["usuario"]="Site"
		except:
			ctx["usuario"]=""
	

	template = loader.get_template('products/lista productos.html')
	
	return HttpResponse(template.render(ctx, request))