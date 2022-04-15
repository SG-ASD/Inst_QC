# Generated by Django 4.0.3 on 2022-04-06 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Instrumentapp', '0002_alter_instrument_sn'),
    ]

    operations = [
        migrations.AddField(
            model_name='instrument',
            name='Computer_SN',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='instrument',
            name='FV2_Version',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='instrument',
            name='FW_Master',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='instrument',
            name='FW_PipetteCh',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='instrument',
            name='FW_Xdrive',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='instrument',
            name='Inspector',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='instrument',
            name='Revision',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='instrument',
            name='SW_Version',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='instrument',
            name='Status',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]