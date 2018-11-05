from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.template import loader


def Index(request):
	ctx={}
	template = loader.get_template('sites/index.html')

	return HttpResponse(template.render(ctx, request))
	
def Logout(request):
	if request.user is not None:

		logout(request)
	return redirect('index')