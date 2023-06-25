from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/', include('account.urls')),
    path('api/patients/', include('patient.urls')),
    path('api/filter/', include('filter.urls')),
    path('admin/', admin.site.urls),
]
