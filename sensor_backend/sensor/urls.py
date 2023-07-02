from django.urls import path
from . import api

urlpatterns = [
    path('heart_rate/', api.heart_rate_list, name='heart_rate'),
    path('blood_cholesterol/', api.blood_cholesterol_list, name='blood_cholesterol'),
    path('blood_glucose/', api.blood_glucose_list, name='blood_glucose'),
    path('blood_pressure/', api.blood_pressure_list, name='blood_pressure'),
    path('parkinson/', api.parkinson_list, name='parkinson'),
    path('temperature/', api.temperature_list, name='temperature'),
    path('respiration_rate/', api.respiration_rate_list, name='respiration_rate'),
]
