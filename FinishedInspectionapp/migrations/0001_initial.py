# Generated by Django 3.2.5 on 2022-07-21 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Instrumentapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FinishInspection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=60)),
                ('Computer_SN', models.CharField(blank=True, max_length=50)),
                ('Barcode_Scanner', models.CharField(blank=True, max_length=50)),
                ('Inspector', models.CharField(blank=True, max_length=20)),
                ('Start_Date', models.DateField(blank=True, null=True)),
                ('Completed_Date', models.DateField(blank=True, null=True)),
                ('SW_Version', models.CharField(blank=True, max_length=50)),
                ('SL_Version', models.CharField(blank=True, max_length=50)),
                ('Revision', models.CharField(blank=True, max_length=50)),
                ('Status', models.CharField(blank=True, max_length=20)),
                ('Computer_Version', models.CharField(blank=True, max_length=50)),
                ('SL_Install', models.CharField(blank=True, max_length=20)),
                ('Method_Import', models.CharField(blank=True, max_length=20)),
                ('SL_Run_Version', models.CharField(blank=True, max_length=20)),
                ('SL_Maintenance_Screen', models.CharField(blank=True, max_length=20)),
                ('SL_Home_Screen', models.CharField(blank=True, max_length=20)),
                ('SL_mode', models.CharField(blank=True, max_length=20)),
                ('SL_Protocol', models.CharField(blank=True, max_length=20)),
                ('SL_Setting_Screen', models.CharField(blank=True, max_length=20)),
                ('SL_Trace', models.CharField(blank=True, max_length=20)),
                ('Condition', models.CharField(blank=True, max_length=20)),
                ('HHS_Labeled', models.CharField(blank=True, max_length=20)),
                ('Acc_Labeled', models.CharField(blank=True, max_length=20)),
                ('Labeling_Instruction_Rev', models.CharField(blank=True, max_length=50)),
                ('Labeling_Instruction', models.CharField(blank=True, max_length=50)),
                ('Labeling_Box', models.CharField(blank=True, max_length=50)),
                ('Label_SN', models.CharField(blank=True, max_length=50)),
                ('Label_MFG', models.CharField(blank=True, max_length=20)),
                ('Label_Option', models.CharField(blank=True, max_length=20)),
                ('UDI_Barcode', models.CharField(blank=True, max_length=20)),
                ('UDI_HRI', models.CharField(blank=True, max_length=20)),
                ('Instrument_SN', models.ForeignKey(db_column='Instrument_SN', on_delete=django.db.models.deletion.CASCADE, related_name='Finished_Instrument_SN', to='Instrumentapp.instrument')),
            ],
        ),
    ]
