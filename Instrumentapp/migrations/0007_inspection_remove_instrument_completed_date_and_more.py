# Generated by Django 4.0.3 on 2022-04-07 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Instrumentapp', '0006_alter_instrument_completed_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inspection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SN', models.CharField(max_length=30, unique=True)),
                ('Name', models.CharField(max_length=60)),
                ('Computer_SN', models.CharField(blank=True, max_length=30)),
                ('Start_Date', models.CharField(blank=True, max_length=30)),
                ('Completed_Date', models.CharField(blank=True, max_length=30)),
                ('Inspector', models.CharField(blank=True, max_length=30)),
                ('Status', models.CharField(blank=True, max_length=30)),
                ('Revision', models.CharField(blank=True, max_length=40)),
                ('SW_Version', models.CharField(blank=True, max_length=30)),
                ('FV2_Version', models.CharField(blank=True, max_length=30)),
                ('FW_PipetteCh', models.CharField(blank=True, max_length=40)),
                ('FW_Xdrive', models.CharField(blank=True, max_length=40)),
                ('FW_Master', models.CharField(blank=True, max_length=40)),
            ],
        ),
        migrations.RemoveField(
            model_name='instrument',
            name='Completed_Date',
        ),
        migrations.RemoveField(
            model_name='instrument',
            name='Computer_SN',
        ),
        migrations.RemoveField(
            model_name='instrument',
            name='FV2_Version',
        ),
        migrations.RemoveField(
            model_name='instrument',
            name='FW_Master',
        ),
        migrations.RemoveField(
            model_name='instrument',
            name='FW_PipetteCh',
        ),
        migrations.RemoveField(
            model_name='instrument',
            name='FW_Xdrive',
        ),
        migrations.RemoveField(
            model_name='instrument',
            name='Inspector',
        ),
        migrations.RemoveField(
            model_name='instrument',
            name='Revision',
        ),
        migrations.RemoveField(
            model_name='instrument',
            name='SW_Version',
        ),
        migrations.RemoveField(
            model_name='instrument',
            name='Start_Date',
        ),
        migrations.RemoveField(
            model_name='instrument',
            name='Status',
        ),
    ]
