# Generated by Django 4.0.3 on 2022-04-06 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Instrumentapp', '0005_alter_instrument_completed_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instrument',
            name='Completed_Date',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]