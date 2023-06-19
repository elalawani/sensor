from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .serializers import PatientSerializer
from .models import Patient
from .forms import PatientForm


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def patient_list(request):
    patients = Patient.objects.all()

    serializer = PatientSerializer(patients, many=True, context={'request': request})

    return JsonResponse(serializer.data, safe=False)


@api_view(['POST'])
def add_patient(request):
    print('test', request.user)

    print(request.data)
    form = PatientForm(request.data)
    message = 'success'
    if form.is_valid():
        patient = form.save(commit=False)
        patient.created_by = request.user
        patient.save()

    else:
        message = 'error'

    return JsonResponse({'message': message})
