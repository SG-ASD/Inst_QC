# Generated by Django 4.0.3 on 2022-05-11 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hardwareapp', '0004_rename_tool_machine_calibration_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='calibration',
            name='Calibration_Serial',
            field=models.CharField(blank=True, max_length=60),
        ),
    ]
