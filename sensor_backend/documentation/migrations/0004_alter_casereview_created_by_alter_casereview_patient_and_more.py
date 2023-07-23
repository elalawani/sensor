# Generated by Django 4.2.2 on 2023-07-19 17:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0005_remove_bloodglucosemeasurement_patient_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('documentation', '0003_rename_centre_pick_initialexamination_centrepick_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casereview',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_creator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='casereview',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_patient', to='patient.patient'),
        ),
        migrations.AlterField(
            model_name='casereviewcouncil',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_creator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='casereviewcouncil',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_patient', to='patient.patient'),
        ),
        migrations.AlterField(
            model_name='casereviewnursecouncil',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_creator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='casereviewnursecouncil',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_patient', to='patient.patient'),
        ),
        migrations.AlterField(
            model_name='consultation',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_creator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='consultation',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_patient', to='patient.patient'),
        ),
        migrations.AlterField(
            model_name='datareviewprocessing',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_creator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='datareviewprocessing',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_patient', to='patient.patient'),
        ),
        migrations.AlterField(
            model_name='initialexamination',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_creator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='initialexamination',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_patient', to='patient.patient'),
        ),
        migrations.AlterField(
            model_name='initialinterviewtelephone',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_creator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='initialinterviewtelephone',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_patient', to='patient.patient'),
        ),
        migrations.AlterField(
            model_name='instructionwearable',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_creator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='instructionwearable',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_patient', to='patient.patient'),
        ),
        migrations.AlterField(
            model_name='telephoneconsultation',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_creator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='telephoneconsultation',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_patient', to='patient.patient'),
        ),
        migrations.AlterField(
            model_name='visit',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_creator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='visit',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_patient', to='patient.patient'),
        ),
    ]
