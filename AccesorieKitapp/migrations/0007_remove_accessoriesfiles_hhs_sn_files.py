# Generated by Django 4.0.3 on 2022-07-14 03:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AccesorieKitapp', '0006_remove_accessoriesfiles_needle_lot_files'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accessoriesfiles',
            name='HHS_SN_Files',
        ),
    ]
