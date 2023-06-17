from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .serializers import PatientSerializer
from .models import Patient
from .forms import PatientForm


@api_view(['GET'])
def patient_list(request):
    patients = Patient.objects.all()

    serializer = PatientSerializer(patients, many=True, context={'request': request})

    return JsonResponse(serializer.data, safe=False)


@api_view(['POST'])
def add_patient(reguest):

    form = PatientForm(reguest.data)

    if form.is_valid():
        patient = form.save(commit=False)
        patient.created_by = reguest.user
        patient.save()

    return JsonResponse({'nasri': 'nasri'})
