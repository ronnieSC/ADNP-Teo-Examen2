from django import forms

from .models import Destination

class DestinationForm(forms.ModelForm):
	class Meta:
		model 	= Destination
		fields 	= [
			'name',
			'img',
			'desc',
			'price',
			'offer',
			'action',
		]

class RawDestinationForm(forms.Form):
	name	= forms.CharField()
	img 	= forms.ImageField(required=False)
	desc 	= forms.CharField()
	price 	= forms.IntegerField()
	offer 	= forms.BooleanField()
	action	= forms.CharField()