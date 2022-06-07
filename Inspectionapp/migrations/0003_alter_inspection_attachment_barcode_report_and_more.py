# Generated by Django 4.0.3 on 2022-06-07 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inspectionapp', '0002_inspection_category_remove_inspection_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inspection',
            name='Attachment_Barcode_Report',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='Attachment_CoverSafety_Report',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='Attachment_Declaration',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='Attachment_Declaration_HHS',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='Attachment_ElectricalSafety_Report',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='Attachment_Measurement_Protocol',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='Attachment_Position_Report',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
