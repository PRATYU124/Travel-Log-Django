from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_trip, name='create_trip'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('trip/<int:trip_id>/map/', views.trip_map, name='trip_map'),
]

