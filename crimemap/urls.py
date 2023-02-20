from django.urls import path
from . import views

urlpatterns = [
    path('crime_map', views.crime_map, name='crime_map'),
]
