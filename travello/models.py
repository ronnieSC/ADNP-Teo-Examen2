from django.db import models

# Create your models here.

'''
class Destination:
	id		: int
	name	: str
	img		: str
	desc	: str
	price	: int
	offer	: bool
'''
class Destination(models.Model):
	name	= models.CharField(max_length=100)
	img 	= models.ImageField(upload_to='pics', null=True, blank=True)
	desc 	= models.CharField(max_length=500)
	price 	= models.IntegerField()
	offer 	= models.BooleanField(default=False)
	action	= models.CharField(max_length=20)