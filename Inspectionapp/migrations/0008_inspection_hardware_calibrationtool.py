# Generated by Django 4.0.3 on 2022-04-15 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inspectionapp', '0007_remove_inspection_hardware_calibrationtool'),
    ]

    operations = [
        migrations.AddField(
            model_name='inspection',
            name='HardWare_CalibrationTool',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]