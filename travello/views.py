from django.shortcuts import render
from .models import Destination

from .forms import RawDestinationForm

# Create your views here.

def index(request):

	dests = Destination.objects.all()

	return render(request, 'index.html', {'dests': dests})

def agregarDestino(request):
	form = RawDestinationForm()

	if request.method =='POST':
		form = RawDestinationForm(request.POST)

		if form.is_valid():
			Destination.objects.create(**form.cleaned_data)

	context = {
		'form': form,
	}

	return render(request, 'formulario_agregarDestino.html', context)