# Generated by Django 4.0.3 on 2022-04-13 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appearanceapp', '0003_rename_image_appearance_binding_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='appearance',
            name='Video',
            field=models.FileField(null=True, upload_to='video/'),
        ),
    ]