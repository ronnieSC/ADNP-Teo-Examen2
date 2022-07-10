from django.shortcuts import render, redirect

from django.http import HttpResponse

#from django.contrib.auth.models import User, auth

# Create your views here.

def arequipa(request):
	if request.user.is_authenticated:
		direccion = 'arequipa.html'

		return render(request, direccion)
	else:
		return redirect('login')

def trujillo(request):
	if request.user.is_authenticated:
		direccion = 'trujillo.html'

		return render(request, direccion)
	else:
		return redirect('login')

def iquitos(request):
	if request.user.is_authenticated:
		direccion = 'iquitos.html'

		return render(request, direccion)
	else:
		return redirect('login')

def cartagena(request):
	if request.user.is_authenticated:
		direccion = 'cartagena.html'

		return render(request, direccion)
	else:
		return redirect('login')