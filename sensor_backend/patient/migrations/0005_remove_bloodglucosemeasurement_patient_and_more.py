# Generated by Django 4.2.2 on 2023-06-29 22:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0004_patient_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bloodglucosemeasurement',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='bloodpressuremeasurement',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='heartratemeasurement',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='respirationratemeasurement',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='sleepmeasurement',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='temperaturemeasurement',
            name='patient',
        ),
        migrations.DeleteModel(
            name='BloodCholesterolMeasurement',
        ),
        migrations.DeleteModel(
            name='BloodGlucoseMeasurement',
        ),
        migrations.DeleteModel(
            name='BloodPressureMeasurement',
        ),
        migrations.DeleteModel(
            name='HeartRateMeasurement',
        ),
        migrations.DeleteModel(
            name='RespirationRateMeasurement',
        ),
        migrations.DeleteModel(
            name='SleepMeasurement',
        ),
        migrations.DeleteModel(
            name='TemperatureMeasurement',
        ),
    ]
