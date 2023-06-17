from django.urls import path
from . import api

urlpatterns = [
    path('', api.patient_list, name='patient_list'),
    path('create/', api.add_patient, name='add_patient'),
]