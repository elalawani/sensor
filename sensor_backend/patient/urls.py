from django.urls import path
from . import api

urlpatterns = [
    path('', api.patient_list, name='patient_list'),
    path('<uuid:pk>/', api.patient, name='patient_list'),
    path('medications/', api.medications_list, name='medications_list'),
    path('chronic_conditions/', api.chronic_conditions_list, name='chronic_conditions_list'),
    path('create/', api.add_patient, name='add_patient'),
]
