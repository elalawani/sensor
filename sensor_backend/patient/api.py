from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .serializers import PatientSerializer
from .models import Patient


@api_view(['GET'])
def patient_list(request):
    patients = Patient.objects.all()

    serializer = PatientSerializer(patients, many=True, context={'request': request})

    return JsonResponse(serializer.data, safe=False)
