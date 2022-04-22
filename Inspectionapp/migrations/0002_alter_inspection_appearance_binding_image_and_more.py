# Generated by Django 4.0.3 on 2022-04-21 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inspectionapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inspection',
            name='Appearance_Binding_Image',
            field=models.ImageField(blank=True, upload_to='Appearance/'),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='Appearance_Labels_Image',
            field=models.ImageField(blank=True, upload_to='Appearance/'),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='Appearance_Packaging_Box_Image',
            field=models.ImageField(blank=True, upload_to='Appearance/'),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='Appearance_Shock_Watch_Image',
            field=models.ImageField(blank=True, upload_to='Appearance/'),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='Appearance_Transport_Jig_Image',
            field=models.ImageField(blank=True, upload_to='Appearance/'),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='Appearance_Video',
            field=models.FileField(blank=True, upload_to='video/'),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='Appearance_Wooden_Pallet_Image',
            field=models.ImageField(blank=True, upload_to='Appearance/'),
        ),
    ]
