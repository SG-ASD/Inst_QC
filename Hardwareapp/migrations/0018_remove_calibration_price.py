# Generated by Django 4.0.3 on 2022-07-07 00:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Hardwareapp', '0017_calibration_price_alter_calibration_erp_num_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calibration',
            name='Price',
        ),
    ]
