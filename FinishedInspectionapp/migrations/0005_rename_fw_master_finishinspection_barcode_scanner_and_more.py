# Generated by Django 4.0.3 on 2022-05-27 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FinishedInspectionapp', '0004_finishinspection_computer_sn'),
    ]

    operations = [
        migrations.RenameField(
            model_name='finishinspection',
            old_name='FW_Master',
            new_name='Barcode_Scanner',
        ),
        migrations.RenameField(
            model_name='finishinspection',
            old_name='SL_Barcode',
            new_name='HHS_Labeled',
        ),
        migrations.RenameField(
            model_name='finishinspection',
            old_name='SL_Capping',
            new_name='Label_Option',
        ),
        migrations.RenameField(
            model_name='finishinspection',
            old_name='FW_PipetteCh',
            new_name='Labeling_Box',
        ),
        migrations.RenameField(
            model_name='finishinspection',
            old_name='SL_Check_Option',
            new_name='UDI_Barcode',
        ),
        migrations.RenameField(
            model_name='finishinspection',
            old_name='VCMS_Acc_Labeled',
            new_name='UDI_HRI',
        ),
        migrations.RemoveField(
            model_name='finishinspection',
            name='FW_VCMS',
        ),
        migrations.RemoveField(
            model_name='finishinspection',
            name='FW_Xdrive',
        ),
        migrations.RemoveField(
            model_name='finishinspection',
            name='VCMS_Packing',
        ),
        migrations.RemoveField(
            model_name='finishinspection',
            name='VCMS_Pallet_Labeled',
        ),
        migrations.RemoveField(
            model_name='finishinspection',
            name='Warranty_Labeled',
        ),
        migrations.AlterField(
            model_name='finishinspection',
            name='Label_SN',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='finishinspection',
            name='Labeling_Instruction',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='finishinspection',
            name='Labeling_Instruction_Rev',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]