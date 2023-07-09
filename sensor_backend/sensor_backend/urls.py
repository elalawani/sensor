from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/', include('account.urls')),
    path('api/conversation/', include('conversation.urls')),
    path('api/patients/', include('patient.urls')),
    path('api/sensor/', include('sensor.urls')),
    path('admin/', admin.site.urls),
]
