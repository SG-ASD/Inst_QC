# Generated by Django 4.0.3 on 2022-06-09 06:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Inspectionapp', '0002_alter_inspection_hardware_pip_x1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inspection',
            old_name='Completed_Date',
            new_name='CompleteDt',
        ),
    ]