from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
	# path('',views.index, name='index'),
	# path('add',views.add, name='add'),
	path('', views.upload), 
]

