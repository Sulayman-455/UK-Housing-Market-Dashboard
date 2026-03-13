from django.urls import path
from . import views

urlpatterns = [
    path('', views.overview, name='overview'),
    path('regional/', views.regional, name='regional'),
    path('property-types/', views.property_types, name='property_types'),
    path('first-time-buyers/', views.first_time_buyers, name='first_time_buyers'),
]