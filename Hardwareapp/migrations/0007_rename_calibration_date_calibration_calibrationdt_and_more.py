# Generated by Django 4.0.3 on 2022-05-12 02:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Hardwareapp', '0006_calibration_cal_location_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='calibration',
            old_name='Calibration_Date',
            new_name='CalibrationDt',
        ),
        migrations.RenameField(
            model_name='calibration',
            old_name='Validation_Date',
            new_name='ValidationDt',
        ),
    ]