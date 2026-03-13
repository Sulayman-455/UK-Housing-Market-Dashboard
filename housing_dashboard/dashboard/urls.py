from django.urls import path
from . import views

# URL routing for dashboard app - maps each path to its view function

urlpatterns = [
    path('', views.overview, name='overview'),
    path('regional/', views.regional, name='regional'),
    path('property-types/', views.property_types, name='property_types'),
    path('first-time-buyers/', views.first_time_buyers, name='first_time_buyers'),
]