from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from account.models import User
from patient.models import Patient


class Measurement(models.Model):
    comment = models.TextField(null=True)
    rating = models.PositiveSmallIntegerField(null=True, blank=True,
                                              validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_by = models.ForeignKey(User, related_name='creator', on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class HeartRateMeasurement(models.Model):
    HeartRate = models.FloatField(null=True, blank=True)


class BloodPressureMeasurement(models.Model):
    systolic_Pressure = models.FloatField(null=True, blank=True)
    diastolic_Pressure = models.FloatField(null=True, blank=True)


class BloodGlucoseMeasurement(models.Model):
    BloodGlucose = models.FloatField(null=True, blank=True)


class RespirationRateMeasurement(models.Model):
    RespirationRate = models.FloatField(null=True, blank=True)


class TemperatureMeasurement(models.Model):
    Temperature = models.FloatField(null=True, blank=True)


class BloodCholesterolMeasurement(models.Model):
    BloodCholesterol = models.FloatField(null=True, blank=True)
