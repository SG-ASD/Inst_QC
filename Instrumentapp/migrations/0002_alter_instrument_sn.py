# Generated by Django 4.0.3 on 2022-04-01 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Instrumentapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instrument',
            name='SN',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
