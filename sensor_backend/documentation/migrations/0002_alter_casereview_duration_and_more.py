# Generated by Django 4.2.2 on 2023-07-15 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casereview',
            name='duration',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='casereviewcouncil',
            name='duration',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='casereviewnursecouncil',
            name='duration',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='consultation',
            name='duration',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='datareviewprocessing',
            name='duration',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='initialexamination',
            name='duration',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='initialinterviewtelephone',
            name='duration',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='instructionwearable',
            name='duration',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='telephoneconsultation',
            name='duration',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='visit',
            name='duration',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
