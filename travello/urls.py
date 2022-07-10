from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('agregarDestino', views.agregarDestino, name='agregarDestino'),
]