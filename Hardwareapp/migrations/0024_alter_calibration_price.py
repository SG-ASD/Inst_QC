# Generated by Django 4.0.3 on 2022-07-08 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hardwareapp', '0023_calibration_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calibration',
            name='Price',
            field=models.IntegerField(blank=True, null=True, verbose_name='가격'),
        ),
    ]
