# Generated by Django 4.0.3 on 2022-04-06 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Instrumentapp', '0004_instrument_completed_date_instrument_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instrument',
            name='Completed_Date',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='instrument',
            name='Start_Date',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]