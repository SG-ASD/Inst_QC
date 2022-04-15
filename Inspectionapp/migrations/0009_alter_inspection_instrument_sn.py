# Generated by Django 4.0.3 on 2022-04-15 04:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Instrumentapp', '0008_delete_inspection'),
        ('Inspectionapp', '0008_inspection_hardware_calibrationtool'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inspection',
            name='Instrument_SN',
            field=models.ForeignKey(db_column='SN', on_delete=django.db.models.deletion.CASCADE, to='Instrumentapp.instrument'),
        ),
    ]
