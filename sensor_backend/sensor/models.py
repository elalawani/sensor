from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from account.models import User
from patient.models import Patient


class Measurement(models.Model):
    created_by = models.ForeignKey(User, related_name='%(class)s_creator', on_delete=models.CASCADE, null=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=30, null=True)
    code = models.CharField(max_length=255, null=True)
    category = models.CharField(max_length=255, null=True)

    class Meta:
        abstract = True


class HeartRateMeasurement(Measurement):
    HeartRate = models.FloatField(null=True, blank=True)
    unit = models.CharField(max_length=30, default='mg/dL')


class HeartRateMeasurementComments(models.Model):
    text = models.TextField()
    measurement = models.ForeignKey(HeartRateMeasurement, related_name='heart_rate_comments', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='heart_rate_comments_creator', on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)


class BloodPressureMeasurement(Measurement):
    systolic_Pressure = models.FloatField(null=True, blank=True)
    diastolic_Pressure = models.FloatField(null=True, blank=True)
    unit = models.CharField(max_length=30, default='mg/dL')


class BloodPressureMeasurementComments(models.Model):
    text = models.TextField()
    measurement = models.ForeignKey(BloodPressureMeasurement, related_name='blood_pressure_comments', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='blood_pressure_comments_creator', on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)


class BloodGlucoseMeasurement(Measurement):
    BloodGlucose = models.FloatField(null=True, blank=True)
    unit = models.CharField(max_length=30, default='mg/dL')


class BloodGlucoseMeasurementComments(models.Model):
    text = models.TextField()
    measurement = models.ForeignKey(BloodGlucoseMeasurement, related_name='blood_glucose_comments', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='blood_glucose_comments_creator', on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)


class RespirationRateMeasurement(Measurement):
    RespirationRate = models.FloatField(null=True, blank=True)
    unit = models.CharField(max_length=30, default='mg/dL')


class RespirationRateMeasurementComments(models.Model):
    text = models.TextField()
    measurement = models.ForeignKey(RespirationRateMeasurement, related_name='respiration_rate_comments', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='respiration_rate_comments_creator', on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)


class TemperatureMeasurement(Measurement):
    Temperature = models.FloatField(null=True, blank=True)
    unit = models.CharField(max_length=30, default='mg/dL')


class TemperatureMeasurementComments(models.Model):
    text = models.TextField()
    measurement = models.ForeignKey(TemperatureMeasurement, related_name='Temperature_comments', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='Temperature_comments_creator', on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)


class BloodCholesterolMeasurement(Measurement):
    BloodCholesterol = models.FloatField(null=True, blank=True)
    unit = models.CharField(max_length=30, default='mg/dL')


class BloodCholesterolMeasurementComments(models.Model):
    text = models.TextField()
    measurement = models.ForeignKey(BloodCholesterolMeasurement, related_name='blood_cholesterol_comments', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='blood_cholesterol_comments_creator', on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)


class ParkinsonsMeasurement(Measurement):
    TREMOR_SEVERITY_CHOICES = [
        (1, 'Slight'),
        (2, 'Noticeable'),
        (3, 'Moderate'),
        (4, 'Severe'),
    ]
    tremor_severity = models.IntegerField(choices=TREMOR_SEVERITY_CHOICES)
    gait_speed = models.FloatField()
    daily_assessment = models.IntegerField()


class ParkinsonsMeasurementComments(models.Model):
    text = models.TextField()
    measurement = models.ForeignKey(ParkinsonsMeasurement, related_name='parkinson_comments', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='parkinson_comments_creator', on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
