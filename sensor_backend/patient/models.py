import uuid

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from account.models import User


class Surgery(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Medication(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ChronicCondition(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Patient(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'

    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    street = models.CharField(max_length=200)
    nr = models.CharField(max_length=3)
    PLZ = models.CharField(max_length=5)
    city = models.CharField(max_length=200)
    date_of_birth = models.DateField(verbose_name="Date of Birth")
    email = models.EmailField(unique=True, null=True)

    # pip install django-phonenumber-field will use this later

    phone = models.CharField(max_length=12)

    doctors = models.ManyToManyField(User,
                                     related_name='patients_doctor',
                                     limit_choices_to={'role': User.DOCTOR}, blank=True)
    nurses = models.ManyToManyField(User,
                                    related_name='patients_nurse',
                                    limit_choices_to={'role': User.NURSE}, blank=True)
    surgeries = models.ManyToManyField(Surgery, related_name='patients_surgeries', blank=True)
    medications = models.ManyToManyField(Medication, related_name='patients_medications', blank=True)
    reason_of_visiting = models.TextField(blank=True)
    chronicConditions = models.ManyToManyField(ChronicCondition, related_name='patients_chronicConditions', blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


class Conversation(models.Model):
    patient = models.ForeignKey(Patient, related_name='conversations', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Documentation(models.Model):
    text = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class HeartRateMeasurement(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    value = models.PositiveSmallIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(null=True, blank=True)
    evaluation_note = models.PositiveSmallIntegerField(null=True, blank=True,
                                                       validators=[MinValueValidator(1), MaxValueValidator(5)])


class BloodPressureMeasurement(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    value = models.CharField(max_length=100, null=True, blank=True)  # systolic/diastolic
    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(null=True, blank=True)
    evaluation_note = models.PositiveSmallIntegerField(null=True, blank=True,
                                                       validators=[MinValueValidator(1), MaxValueValidator(5)])


class BloodGlucoseMeasurement(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    value = models.PositiveSmallIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(null=True, blank=True)
    evaluation_note = models.PositiveSmallIntegerField(null=True, blank=True,
                                                       validators=[MinValueValidator(1), MaxValueValidator(5)])


class RespirationRateMeasurement(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    value = models.PositiveSmallIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(null=True, blank=True)
    evaluation_note = models.PositiveSmallIntegerField(null=True, blank=True,
                                                       validators=[MinValueValidator(1), MaxValueValidator(5)])


class TemperatureMeasurement(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    value = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(null=True, blank=True)
    evaluation_note = models.PositiveSmallIntegerField(null=True, blank=True,
                                                       validators=[MinValueValidator(1), MaxValueValidator(5)])


class SleepMeasurement(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    value = models.PositiveSmallIntegerField(null=True, blank=True)  # duration in minutes
    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(null=True, blank=True)
    evaluation_note = models.PositiveSmallIntegerField(null=True, blank=True,
                                                       validators=[MinValueValidator(1), MaxValueValidator(5)])


class BloodCholesterolMeasurement(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    value = models.PositiveSmallIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(null=True, blank=True)
    evaluation_note = models.PositiveSmallIntegerField(null=True, blank=True,
                                                       validators=[MinValueValidator(1), MaxValueValidator(5)])




