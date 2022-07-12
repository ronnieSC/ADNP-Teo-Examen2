from django.shortcuts import render

from django.http import HttpResponse
from .utils.sendNotification import sendSumNotification

# Create your views here.

def home(request):
	return render(request, 'home.html', {'name': 'Ronnie'})

def operation(request):

	res = 0

	val1 = int(request.POST['num1'])
	val2 = int(request.POST['num2'])

	operador = request.POST['operacion']
	if operador == "sumar":
		res = val1 + val2
		sendSumNotification(val1, val2, res)
	if operador == "multiplicar":
		res = val1 * val2


	return render(request, 'result.html', {'resultado': res})