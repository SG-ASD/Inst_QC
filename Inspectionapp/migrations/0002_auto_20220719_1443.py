# Generated by Django 3.2.5 on 2022-07-19 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inspectionapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inspection',
            name='Attachment_Barcode_Report_File',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='Attachment_CoverSafety_Report_File',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='Attachment_Files',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='Attachment_Position_Report_File',
            field=models.TextField(blank=True),
        ),
    ]
