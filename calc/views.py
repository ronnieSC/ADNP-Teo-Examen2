from django.shortcuts import render

from django.http import HttpResponse
from .utils.sendNotification import sendSumNotification

# Create your views here.

def home(request):
	return render(request, 'home.html', {'name': 'Ronnie'})

def operation(request):

	message = request.POST['mensaje']

	sendSumNotification(message)


	return render(request, 'result.html', {'resultado': message})
