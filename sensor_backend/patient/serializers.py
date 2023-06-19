from rest_framework import serializers

from .models import Patient, ChronicCondition, Medication
from account.serializers import UserSerializer


class ChronicConditionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChronicCondition
        fields = ['id', 'name']


class MedicationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = ['id', 'name']


class PatientSerializer(serializers.ModelSerializer):
    doctors = UserSerializer(many=True, read_only=True)
    nurses = UserSerializer(many=True, read_only=True)
    chronicConditions = ChronicConditionsSerializer(many=True, read_only=True)
    medications = MedicationsSerializer(many=True, read_only=True)

    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'gender', 'street', 'nr', 'PLZ', 'city', 'phone',
                  'date_of_birth', 'email', 'doctors', 'nurses', 'reason_of_visiting',
                  'chronicConditions', 'medications']
