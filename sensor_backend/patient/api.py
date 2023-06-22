from django.http import JsonResponse, Http404
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .serializers import PatientSerializer, MedicationsSerializer, ChronicConditionsSerializer
from .models import Patient, Medication, ChronicCondition
from .forms import PatientForm


@api_view(['GET'])
def patient_list(request):
    patients = Patient.objects.all()

    serializer = PatientSerializer(patients, many=True, context={'request': request})

    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def patient(request, pk):
    try:
        patients = Patient.objects.get(pk=pk)
    except Patient.DoesNotExist:
        raise Http404

    if request.method == 'GET':
        serializer = PatientSerializer(patients, context={'request': request})
        return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def medications_list(request):
    medications = Medication.objects.all()

    serializer = MedicationsSerializer(medications, many=True, context={'request': request})
    print(serializer.data)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def chronic_conditions_list(request):
    chronic_conditions = ChronicCondition.objects.all()

    serializer = ChronicConditionsSerializer(chronic_conditions, many=True, context={'request': request})
    print(serializer.data)
    return JsonResponse(serializer.data, safe=False)


@api_view(['POST'])
def add_patient(request):
    print('test', request.user)

    print('request.data:', request.data, id)
    form = PatientForm(request.data)
    message = 'success'
    if form.is_valid():
        patient = form.save(commit=False)
        patient.created_by = request.user
        patient.save()
        patient.doctors.set(form.cleaned_data.get('doctors'))
        patient.nurses.set(form.cleaned_data.get('nurses'))
        patient.chronicConditions.set(form.cleaned_data.get('chronicConditions'))
        patient.medications.set(form.cleaned_data.get('medications'))
        patient.save()

    else:
        message = 'error'

    return JsonResponse({'message': message})
