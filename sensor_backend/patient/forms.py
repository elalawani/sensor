from django import forms

from .models import Patient, ChronicCondition, Medication
from account.models import User


class PatientForm(forms.ModelForm):
    doctors = forms.ModelMultipleChoiceField(queryset=User.objects.filter(role='DR'), required=False)
    nurses = forms.ModelMultipleChoiceField(queryset=User.objects.filter(role='NR'), required=False)
    chronicConditions = forms.ModelMultipleChoiceField(queryset=ChronicCondition.objects.all(), required=False)
    medications = forms.ModelMultipleChoiceField(queryset=Medication.objects.all(), required=False)

    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'gender', 'street', 'nr', 'PLZ', 'city', 'phone',
                  'date_of_birth', 'email', 'doctors', 'nurses', 'reason_of_visiting',
                  'chronicConditions', 'medications']
