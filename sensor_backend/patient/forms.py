from django.forms import ModelForm

from .models import Patient


class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'gender', 'street', 'nr', 'PLZ', 'city', 'phone',
                  'date_of_birth', 'email', 'doctors', 'nurses']
