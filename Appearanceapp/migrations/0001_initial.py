# Generated by Django 4.0.3 on 2022-04-12 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appearance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Instrument_SN', models.CharField(max_length=50)),
                ('Shock_Watch', models.CharField(max_length=20, null=True)),
                ('Binding', models.CharField(max_length=20, null=True)),
                ('Labels', models.CharField(max_length=20, null=True)),
                ('Packaging_Box', models.CharField(max_length=20, null=True)),
                ('Wooden_Pallet', models.CharField(max_length=20, null=True)),
                ('Transport_Jig', models.CharField(max_length=20, null=True)),
                ('Front', models.CharField(max_length=20, null=True)),
                ('Right', models.CharField(max_length=20, null=True)),
                ('Left', models.CharField(max_length=20, null=True)),
                ('Back', models.CharField(max_length=20, null=True)),
                ('Acc_Damage', models.CharField(max_length=20, null=True)),
                ('Acc_Missing', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]