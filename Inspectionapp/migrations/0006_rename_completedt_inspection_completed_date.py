# Generated by Django 4.0.3 on 2022-06-13 04:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Inspectionapp', '0005_alter_inspection_start_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inspection',
            old_name='CompleteDt',
            new_name='Completed_Date',
        ),
    ]
