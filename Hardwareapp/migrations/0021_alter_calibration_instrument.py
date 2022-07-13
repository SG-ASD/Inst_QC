# Generated by Django 4.0.3 on 2022-07-07 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hardwareapp', '0020_alter_calibration_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calibration',
            name='Instrument',
            field=models.CharField(choices=[('Seegene STARlet', 'Seegene STARlet'), ('Hamilton STARlet', 'Hamilton STARlet'), ('Seegene Nimbus', 'Seegene Nimbus'), ('CFX 96Dx', 'CFX 96Dx'), ('Seeprep32', 'Seeprep32'), ('SGRT', 'SGRT'), ('AIOS', 'AIOS'), ('VCMS', 'VCMS')], default='가능', max_length=32, verbose_name='상태'),
        ),
    ]
