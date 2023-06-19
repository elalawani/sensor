from django.forms import ModelForm

from .models import Patient
from .serializers import ChronicConditionsSerializer, MedicationsSerializer
from account.serializers import UserSerializer


class PatientForm(ModelForm):
    doctors = UserSerializer(many=True, read_only=True)
    nurses = UserSerializer(many=True, read_only=True)
    chronicConditions = ChronicConditionsSerializer(many=True, read_only=True)
    medications = MedicationsSerializer(many=True, read_only=True)

    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'gender', 'street', 'nr', 'PLZ', 'city', 'phone',
                  'date_of_birth', 'email', 'doctors', 'nurses', 'reason_of_visiting',
                  'chronicConditions', 'medications']
