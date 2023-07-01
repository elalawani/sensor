from rest_framework import serializers
from .models import *


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['nurse', 'patient', 'timestamp', 'comment', 'rating']


class BloodGlucoseMeasurementSerializer(MeasurementSerializer):
    class Meta(MeasurementSerializer.Meta):
        model = BloodGlucoseMeasurement
        fields = MeasurementSerializer.Meta.fields + ['BloodGlucose']


class BloodPressureMeasurementSerializer(MeasurementSerializer):
    class Meta(MeasurementSerializer.Meta):
        model = BloodPressureMeasurement
        fields = MeasurementSerializer.Meta.fields + ['systolic_Pressure', 'diastolic_Pressure']


class HeartRateMeasurementSerializer(MeasurementSerializer):
    class Meta(MeasurementSerializer.Meta):
        model = HeartRateMeasurement
        fields = MeasurementSerializer.Meta.fields + ['HeartRate']


class RespirationRateMeasurementSerializer(MeasurementSerializer):
    class Meta(MeasurementSerializer.Meta):
        model = RespirationRateMeasurement
        fields = MeasurementSerializer.Meta.fields + ['RespirationRate']


class TemperatureMeasurementSerializer(MeasurementSerializer):
    class Meta(MeasurementSerializer.Meta):
        model = TemperatureMeasurement
        fields = MeasurementSerializer.Meta.fields + ['Temperature']


class BloodCholesterolMeasurementSerializer(MeasurementSerializer):
    class Meta(MeasurementSerializer.Meta):
        model = BloodCholesterolMeasurement
        fields = MeasurementSerializer.Meta.fields + ['BloodCholesterol']
