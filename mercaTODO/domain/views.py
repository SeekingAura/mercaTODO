from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth import logout
from django.shortcuts import redirect
from django.template import loader

# Models
from django.contrib.auth.models import User
from sites.models import Site

#Auth control
from django.contrib.auth import authenticate, login

def Index(request):
	ctx={"usuario":""}
	if (request.user.is_authenticated):
		user_id = request.user
		try:
			Site.objects.get(User_id=user_id)
			ctx["usuario"]="Site"
		except:
			pass
	template = loader.get_template('domain/index.html')
	return HttpResponse(template.render(ctx, request))

def Login(request):
	ctx={}
	if (request.user.is_authenticated):
		try:
			Site.objects.get(User_id=user_id)
			return redirect('sites:misProductos')
		except:
			ctx["usuario"]=""
		if(request.user.is_staff):# when uses django admin
			return redirect('domain:logout')
		return redirect('domain:index')
	error=[False, "", "None"]
	ctx["error"]=error
	template = loader.get_template('domain/login.html')
	if(request.method == "POST"):
		if("usernameSitio" in request.POST):
			username = request.POST.get('usernameSitio').lower()
			password = request.POST.get('password')
			usuario = User.objects.filter(username=username)

			if len(usuario) != 0:
				user = authenticate(username=username, password=password)
				if user is not None:
					login(request, user)
					return redirect('sites:misProductos')
				else:
					error = [True, "Contraseña no valida", "Sitio"]
			else:
				error = [True, "No existe el usuario {}".format(username), "Sitio"]
			template = loader.get_template('domain/login.html')

	ctx['error']=error

	


	return HttpResponse(template.render(ctx, request))
	
def Logout(request):
	if request.user is not None:
		logout(request)
	return redirect('domain:index')