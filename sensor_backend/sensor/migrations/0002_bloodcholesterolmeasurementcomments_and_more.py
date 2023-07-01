# Generated by Django 4.2.2 on 2023-07-01 13:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0005_remove_bloodglucosemeasurement_patient_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sensor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BloodCholesterolMeasurementComments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='blood_cholesterol_comments_creator', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BloodGlucoseMeasurementComments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='blood_glucose_comments_creator', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BloodPressureMeasurementComments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='blood_pressure_comments_creator', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HeartRateMeasurementComments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='heart_rate_comments_creator', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ParkinsonsMeasurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(max_length=30, null=True)),
                ('code', models.CharField(max_length=255, null=True)),
                ('category', models.CharField(max_length=255, null=True)),
                ('tremor_severity', models.IntegerField(choices=[(1, 'Slight'), (2, 'Noticeable'), (3, 'Moderate'), (4, 'Severe')])),
                ('gait_speed', models.FloatField()),
                ('daily_assessment', models.IntegerField()),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_creator', to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='patient.patient')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ParkinsonsMeasurementComments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='parkinson_comments_creator', to=settings.AUTH_USER_MODEL)),
                ('measurement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parkinson_comments', to='sensor.parkinsonsmeasurement')),
            ],
        ),
        migrations.CreateModel(
            name='RespirationRateMeasurementComments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='respiration_rate_comments_creator', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TemperatureMeasurementComments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='Temperature_comments_creator', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='bloodcholesterolmeasurement',
            name='category',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='bloodcholesterolmeasurement',
            name='code',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='bloodcholesterolmeasurement',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='bloodcholesterolmeasurement',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_creator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bloodcholesterolmeasurement',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='patient.patient'),
        ),
        migrations.AddField(
            model_name='bloodcholesterolmeasurement',
            name='status',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='bloodcholesterolmeasurement',
            name='unit',
            field=models.CharField(default='mg/dL', max_length=30),
        ),
        migrations.AddField(
            model_name='bloodglucosemeasurement',
            name='category',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='bloodglucosemeasurement',
            name='code',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='bloodglucosemeasurement',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='bloodglucosemeasurement',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_creator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bloodglucosemeasurement',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='patient.patient'),
        ),
        migrations.AddField(
            model_name='bloodglucosemeasurement',
            name='status',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='bloodglucosemeasurement',
            name='unit',
            field=models.CharField(default='mg/dL', max_length=30),
        ),
        migrations.AddField(
            model_name='bloodpressuremeasurement',
            name='category',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='bloodpressuremeasurement',
            name='code',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='bloodpressuremeasurement',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='bloodpressuremeasurement',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_creator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bloodpressuremeasurement',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='patient.patient'),
        ),
        migrations.AddField(
            model_name='bloodpressuremeasurement',
            name='status',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='bloodpressuremeasurement',
            name='unit',
            field=models.CharField(default='mg/dL', max_length=30),
        ),
        migrations.AddField(
            model_name='heartratemeasurement',
            name='category',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='heartratemeasurement',
            name='code',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='heartratemeasurement',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='heartratemeasurement',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_creator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='heartratemeasurement',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='patient.patient'),
        ),
        migrations.AddField(
            model_name='heartratemeasurement',
            name='status',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='heartratemeasurement',
            name='unit',
            field=models.CharField(default='mg/dL', max_length=30),
        ),
        migrations.AddField(
            model_name='respirationratemeasurement',
            name='category',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='respirationratemeasurement',
            name='code',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='respirationratemeasurement',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='respirationratemeasurement',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_creator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='respirationratemeasurement',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='patient.patient'),
        ),
        migrations.AddField(
            model_name='respirationratemeasurement',
            name='status',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='respirationratemeasurement',
            name='unit',
            field=models.CharField(default='mg/dL', max_length=30),
        ),
        migrations.AddField(
            model_name='temperaturemeasurement',
            name='category',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='temperaturemeasurement',
            name='code',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='temperaturemeasurement',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='temperaturemeasurement',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_creator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='temperaturemeasurement',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='patient.patient'),
        ),
        migrations.AddField(
            model_name='temperaturemeasurement',
            name='status',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='temperaturemeasurement',
            name='unit',
            field=models.CharField(default='mg/dL', max_length=30),
        ),
        migrations.DeleteModel(
            name='Measurement',
        ),
        migrations.AddField(
            model_name='temperaturemeasurementcomments',
            name='measurement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Temperature_comments', to='sensor.temperaturemeasurement'),
        ),
        migrations.AddField(
            model_name='respirationratemeasurementcomments',
            name='measurement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='respiration_rate_comments', to='sensor.respirationratemeasurement'),
        ),
        migrations.AddField(
            model_name='heartratemeasurementcomments',
            name='measurement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='heart_rate_comments', to='sensor.heartratemeasurement'),
        ),
        migrations.AddField(
            model_name='bloodpressuremeasurementcomments',
            name='measurement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blood_pressure_comments', to='sensor.bloodpressuremeasurement'),
        ),
        migrations.AddField(
            model_name='bloodglucosemeasurementcomments',
            name='measurement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blood_glucose_comments', to='sensor.bloodglucosemeasurement'),
        ),
        migrations.AddField(
            model_name='bloodcholesterolmeasurementcomments',
            name='measurement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blood_cholesterol_comments', to='sensor.bloodcholesterolmeasurement'),
        ),
    ]
