from django.urls import path
from . import api

urlpatterns = [
    path('heart_rate/', api.post_heart_rate, name='post_heart_rate'),
    path('heart_rate/<uuid:patient_id>', api.get_heart_rate, name='get_heart_rate'),
    path('blood_cholesterol/', api.post_blood_cholesterol, name='post_blood_cholesterol'),
    path('blood_cholesterol/<uuid:patient_id>', api.get_blood_cholesterol, name='get_blood_cholesterol'),
    path('blood_glucose/', api.post_blood_glucose, name='post_blood_glucose'),
    path('blood_glucose/<uuid:patient_id>', api.get_blood_glucose, name='get_blood_glucose'),
    path('blood_pressure/', api.post_blood_pressure, name='post_blood_pressure'),
    path('blood_pressure/<uuid:patient_id>', api.get_blood_pressure, name='get_blood_pressure'),
    path('parkinson/', api.post_parkinson, name='post_parkinson'),
    path('parkinson/<uuid:patient_id>', api.get_parkinson, name='get_parkinson'),
    path('temperature/', api.post_temperature, name='post_temperature'),
    path('temperature/<uuid:patient_id>', api.get_temperature, name='get_temperature'),
    path('respiration_rate/', api.post_respiration_rate, name='post_respiration_rate'),
    path('respiration_rate/<uuid:patient_id>', api.get_respiration_rate, name='get_respiration_rate'),
]
