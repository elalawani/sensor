from rest_framework import serializers

from .models import Patient
from account.serializers import UserSerializer


class PatientSerializer(serializers.ModelSerializer):
    doctors = UserSerializer(many=True, read_only=True)
    nurses = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'gender', 'street', 'nr', 'PLZ', 'city', 'phone',
                  'date_of_birth', 'email', 'doctors', 'nurses']
