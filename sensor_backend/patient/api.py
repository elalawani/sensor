from django.http import JsonResponse, Http404
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.core.exceptions import PermissionDenied
from rest_framework.permissions import IsAdminUser

from conversation.models import Conversation
from .filters import PatientFilter
from .serializers import PatientSerializer, MedicationsSerializer, ChronicConditionsSerializer
from .models import Patient, Medication, ChronicCondition
from .forms import PatientForm


@api_view(['GET'])
def patient_list(request):
    user = request.user
    if user.role == 'ST':
        patients = Patient.objects.all().distinct()
    elif user.role == 'DR':
        patients = Patient.objects.filter(doctors=user).distinct()
    elif user.role == 'NR':
        patients = Patient.objects.filter(nurses=user).distinct()
    else:
        raise PermissionDenied("You do not have permission to views patients.")

    filtered = PatientFilter(request.GET, queryset=patients)

    serializer = PatientSerializer(filtered.qs, many=True, context={'request': request})

    print(request.GET)

    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def patient(request, pk):
    user = request.user
    try:
        patient_info = Patient.objects.get(pk=pk)
    except Patient.DoesNotExist:
        raise Http404("Patient does not exist.")

    if user.role == 'ST':
        pass
    elif user.role == 'DR':
        if not Patient.objects.filter(doctors=user, pk=pk).exists():
            raise PermissionDenied("You do not have permission to views patients.")
    elif user.role == 'NR':
        if not Patient.objects.filter(nurses=user, pk=pk).exists():
            raise PermissionDenied("You do not have permission to views patients.")
    else:
        raise PermissionDenied("You do not have permission to views patients.")

    if request.method == 'GET':
        serializer = PatientSerializer(patient_info, context={'request': request})
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
@permission_classes([IsAdminUser])
def add_patient(request):
    print('request.data:', request.data, id)
    form = PatientForm(request.data)
    message = 'success'
    if form.is_valid():
        patient = form.save(commit=False)
        patient.created_by = request.user
        patient.save()
        doctors = form.cleaned_data.get('doctors')
        nurses = form.cleaned_data.get('nurses')
        patient.doctors.set(doctors)
        patient.nurses.set(nurses)
        patient.chronicConditions.set(form.cleaned_data.get('chronicConditions'))
        patient.medications.set(form.cleaned_data.get('medications'))

        conversation = Conversation.objects.create(patient=patient)

        for user in list(doctors) + list(nurses):
            conversation.users.add(user)

        patient.save()

    else:
        message = 'error'

    return JsonResponse({'message': message})
