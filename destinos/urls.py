from django.urls import path

from . import views

urlpatterns = [
	path('arequipa', views.arequipa, name='arequipa'),
	path('trujillo', views.trujillo, name='trujillo'),
	path('iquitos', views.iquitos, name='iquitos'),
	path('cartagena', views.cartagena, name='cartagena'),
]