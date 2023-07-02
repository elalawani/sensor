from rest_framework import serializers
from .models import *


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['created_by', 'created_at', 'status', 'patient', 'code', 'category']


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['text', 'created_by', 'created_at']
        abstract = True


class ParkinsonsMeasurementSerializer(MeasurementSerializer):
    class Meta(MeasurementSerializer.Meta):
        model = ParkinsonsMeasurement
        fields = MeasurementSerializer.Meta.fields + ['tremor_severity', 'gait_speed', 'daily_assessment']


class ParkinsonsMeasurementCommentSerializer(CommentsSerializer):
    measurement = ParkinsonsMeasurementSerializer()

    class Meta:
        model = ParkinsonsMeasurementComments
        fields = CommentsSerializer.Meta.fields + ['measurement']


class BloodGlucoseMeasurementSerializer(MeasurementSerializer):
    class Meta(MeasurementSerializer.Meta):
        model = BloodGlucoseMeasurement
        fields = MeasurementSerializer.Meta.fields + ['BloodGlucose', 'unit']


class BloodGlucoseMeasurementCommentSerializer(CommentsSerializer):
    measurement = BloodGlucoseMeasurementSerializer()

    class Meta:
        model = BloodGlucoseMeasurement
        fields = CommentsSerializer.Meta.fields + ['measurement']


class BloodPressureMeasurementSerializer(MeasurementSerializer):
    class Meta(MeasurementSerializer.Meta):
        model = BloodPressureMeasurement
        fields = MeasurementSerializer.Meta.fields + ['systolic_Pressure', 'diastolic_Pressure', 'unit']


class BloodPressureMeasurementCommentSerializer(CommentsSerializer):
    measurement = BloodPressureMeasurementSerializer()

    class Meta:
        model = BloodPressureMeasurement
        fields = CommentsSerializer.Meta.fields + ['measurement']


class HeartRateMeasurementSerializer(MeasurementSerializer):
    class Meta(MeasurementSerializer.Meta):
        model = HeartRateMeasurement
        fields = MeasurementSerializer.Meta.fields + ['HeartRate', 'unit']


class HeartRateMeasurementCommentSerializer(CommentsSerializer):
    measurement = HeartRateMeasurementSerializer()

    class Meta:
        model = HeartRateMeasurement
        fields = CommentsSerializer.Meta.fields + ['measurement']


class RespirationRateMeasurementSerializer(MeasurementSerializer):
    class Meta(MeasurementSerializer.Meta):
        model = RespirationRateMeasurement
        fields = MeasurementSerializer.Meta.fields + ['RespirationRate', 'unit']


class RespirationRateMeasurementCommentSerializer(CommentsSerializer):
    measurement = RespirationRateMeasurementSerializer()

    class Meta:
        model = RespirationRateMeasurement
        fields = CommentsSerializer.Meta.fields + ['measurement']


class TemperatureMeasurementSerializer(MeasurementSerializer):
    class Meta(MeasurementSerializer.Meta):
        model = TemperatureMeasurement
        fields = MeasurementSerializer.Meta.fields + ['Temperature', 'unit']


class TemperatureMeasurementCommentSerializer(CommentsSerializer):
    measurement = TemperatureMeasurementSerializer()

    class Meta:
        model = TemperatureMeasurement
        fields = CommentsSerializer.Meta.fields + ['measurement']


class BloodCholesterolMeasurementSerializer(MeasurementSerializer):
    class Meta(MeasurementSerializer.Meta):
        model = BloodCholesterolMeasurement
        fields = MeasurementSerializer.Meta.fields + ['BloodCholesterol', 'unit']


class BloodCholesterolMeasurementCommentSerializer(CommentsSerializer):
    measurement = BloodCholesterolMeasurementSerializer()

    class Meta:
        model = BloodCholesterolMeasurement
        fields = CommentsSerializer.Meta.fields + ['measurement']
