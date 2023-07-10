from django.urls import path
from . import api

urlpatterns = [
    path('', api.task_list, name='task_list'),
    path('create/', api.task_create, name='task_create'),
    path('update/<uuid:pk>/', api.task_update, name='task_update'),
    path('delete/<uuid:pk>/', api.task_delete, name='task_delete'),
]
