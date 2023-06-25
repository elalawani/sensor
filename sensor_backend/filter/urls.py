from django.urls import path
from . import api
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', api.filter, name='filter'),
]
