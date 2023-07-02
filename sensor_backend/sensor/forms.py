from django import forms
from models import *


class MeasurementForm(forms.ModelForm):
    class Meta:
        model = Measurement
        fields = ['created_by', 'patient', 'comment', 'rating']


class BloodGlucoseMeasurementForm(MeasurementForm):
    class Meta(MeasurementForm.Meta):
        model = BloodGlucoseMeasurement
        fields = MeasurementForm.Meta.fields + ['BloodGlucose']


class BloodPressureMeasurementForm(MeasurementForm):
    class Meta(MeasurementForm.Meta):
        model = BloodPressureMeasurement
        fields = MeasurementForm.Meta.fields + ['systolic_Pressure', 'diastolic_Pressure']


class HeartRateMeasurementForm(MeasurementForm):
    class Meta(MeasurementForm.Meta):
        model = HeartRateMeasurement
        fields = MeasurementForm.Meta.fields + ['HeartRate']


class RespirationRateMeasurementForm(MeasurementForm):
    class Meta(MeasurementForm.Meta):
        model = RespirationRateMeasurement
        fields = MeasurementForm.Meta.fields + ['RespirationRate']


class TemperatureMeasurementForm(MeasurementForm):
    class Meta(MeasurementForm.Meta):
        model = TemperatureMeasurement
        fields = MeasurementForm.Meta.fields + ['Temperature']


class BloodCholesterolMeasurementForm(MeasurementForm):
    class Meta(MeasurementForm.Meta):
        model = BloodCholesterolMeasurement
        fields = MeasurementForm.Meta.fields + ['BloodCholesterol']
