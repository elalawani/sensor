from django.contrib import admin

from .models import \
    Patient, Medication, Conversation, \
    ChronicCondition, Surgery, Documentation

admin.site.register(Patient)
admin.site.register(Medication)
admin.site.register(Conversation)
admin.site.register(ChronicCondition)
admin.site.register(Surgery)
admin.site.register(Documentation)
