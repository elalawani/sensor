from django.contrib import admin

from .models import \
    Patient, Medication, Conversation, \
    ChronicCondition, BloodCholesterolMeasurement, TemperatureMeasurement, \
    SleepMeasurement, BloodGlucoseMeasurement, BloodPressureMeasurement, HeartRateMeasurement, \
    RespirationRateMeasurement, Surgery, Documentation

admin.site.register(Patient)
admin.site.register(Medication)
admin.site.register(Conversation)
admin.site.register(BloodCholesterolMeasurement)
admin.site.register(ChronicCondition)
admin.site.register(TemperatureMeasurement)
admin.site.register(SleepMeasurement)
admin.site.register(BloodGlucoseMeasurement)
admin.site.register(BloodPressureMeasurement)
admin.site.register(HeartRateMeasurement)
admin.site.register(RespirationRateMeasurement)
admin.site.register(Surgery)
admin.site.register(Documentation)
