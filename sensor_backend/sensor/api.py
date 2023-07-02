from django.http import JsonResponse, Http404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from django.core.exceptions import PermissionDenied
from rest_framework.response import Response

from .serializers import *
from .models import *


@api_view(['POST', 'GET'])
def heart_rate_list(request):
    if request.method == 'POST':
        serializer = HeartRateMeasurementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        heart_rate = HeartRateMeasurement.objects.all()
        serializer = HeartRateMeasurementSerializer(heart_rate, many=True)
        return Response(serializer.data)


@api_view(['POST', 'GET'])
def blood_pressure_list(request):
    if request.method == 'POST':
        serializer = BloodPressureMeasurementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        blood_pressure = BloodPressureMeasurement.objects.all()
        serializer = BloodPressureMeasurementSerializer(blood_pressure, many=True)
        return Response(serializer.data)


@api_view(['POST', 'GET'])
def blood_glucose_list(request):
    if request.method == 'POST':
        serializer = BloodGlucoseMeasurementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        blood_glucose = BloodGlucoseMeasurement.objects.all()
        serializer = BloodGlucoseMeasurementSerializer(blood_glucose, many=True)
        return Response(serializer.data)


@api_view(['POST', 'GET'])
def respiration_rate_list(request):
    if request.method == 'POST':
        serializer = RespirationRateMeasurementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        respiration_rate = RespirationRateMeasurement.objects.all()
        serializer = RespirationRateMeasurementSerializer(respiration_rate, many=True)
        return Response(serializer.data)


@api_view(['POST', 'GET'])
@permission_classes([])
def temperature_list(request):
    print('request.data:', request.data, id)
    if request.method == 'POST':
        serializer = TemperatureMeasurementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        temperature = TemperatureMeasurement.objects.all()
        serializer = TemperatureMeasurementSerializer(temperature, many=True)
        print('temperature:', serializer.data)
        return Response(serializer.data)


@api_view(['POST', 'GET'])
def blood_cholesterol_list(request):
    if request.method == 'POST':
        serializer = BloodCholesterolMeasurementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        blood_cholesterol = BloodCholesterolMeasurement.objects.all()
        serializer = BloodCholesterolMeasurementSerializer(blood_cholesterol, many=True)
        return Response(serializer.data)


@api_view(['POST', 'GET'])
def parkinson_list(request):
    if request.method == 'POST':
        serializer = ParkinsonsMeasurementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        parkinson = ParkinsonsMeasurement.objects.all()
        serializer = ParkinsonsMeasurementSerializer(parkinson, many=True)
        return Response(serializer.data)
