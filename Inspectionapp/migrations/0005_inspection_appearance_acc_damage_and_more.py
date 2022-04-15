# Generated by Django 4.0.3 on 2022-04-15 04:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Instrumentapp', '0008_delete_inspection'),
        ('Inspectionapp', '0004_alter_inspection_computer_sn_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='inspection',
            name='Appearance_Acc_Damage',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='inspection',
            name='Appearance_Acc_Missing',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='inspection',
            name='Appearance_Back',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='inspection',
            name='Appearance_Binding',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='inspection',
            name='Appearance_Binding_Image',
            field=models.ImageField(blank=True, null=True, upload_to='Appearance/'),
        ),
        migrations.AddField(
            model_name='inspection',
            name='Appearance_Front',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='inspection',
            name='Appearance_Labels',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='inspection',
            name='Appearance_Labels_Image',
            field=models.ImageField(blank=True, null=True, upload_to='Appearance/'),
        ),
        migrations.AddField(
            model_name='inspection',
            name='Appearance_Left',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='inspection',
            name='Appearance_Packaging_Box',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='inspection',
            name='Appearance_Packaging_Box_Image',
            field=models.ImageField(blank=True, null=True, upload_to='Appearance/'),
        ),
        migrations.AddField(
            model_name='inspection',
            name='Appearance_Right',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='inspection',
            name='Appearance_Shock_Watch',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='inspection',
            name='Appearance_Shock_Watch_Image',
            field=models.ImageField(blank=True, null=True, upload_to='Appearance/'),
        ),
        migrations.AddField(
            model_name='inspection',
            name='Appearance_Top',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='inspection',
            name='Appearance_Transport_Jig',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='inspection',
            name='Appearance_Transport_Jig_Image',
            field=models.ImageField(blank=True, null=True, upload_to='Appearance/'),
        ),
        migrations.AddField(
            model_name='inspection',
            name='Appearance_Video',
            field=models.FileField(blank=True, null=True, upload_to='video/'),
        ),
        migrations.AddField(
            model_name='inspection',
            name='Appearance_Wooden_Pallet',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='inspection',
            name='Appearance_Wooden_Pallet_Image',
            field=models.ImageField(blank=True, null=True, upload_to='Appearance/'),
        ),
        migrations.AddField(
            model_name='inspection',
            name='Attachment_Barcode_Report',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='inspection',
            name='Attachment_Barcode_Report_File',
            field=models.FileField(blank=True, null=True, upload_to='report/'),
        ),
        migrations.AddField(
            model_name='inspection',
            name='Attachment_CoverSafety_Report',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='inspection',
            name='Attachment_CoverSafety_Report_File',
            field=models.FileField(blank=True, null=True, upload_to='report/'),
        ),
        migrations.AddField(
            model_name='inspection',
            name='Attachment_Declaration',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='inspection',
            name='Attachment_Declaration_HHS',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='inspection',
            name='Attachment_ElectricalSafety_Report',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='inspection',
            name='Attachment_Files',
            field=models.FileField(blank=True, null=True, upload_to='report/'),
        ),
        migrations.AddField(
            model_name='inspection',
            name='Attachment_Measurement_Protocol',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='inspection',
            name='Attachment_Position_Report',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='inspection',
            name='Attachment_Position_Report_File',
            field=models.FileField(blank=True, null=True, upload_to='report/'),
        ),
        migrations.AddField(
            model_name='inspection',
            name='ElectricalTest_GroundResistance',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='inspection',
            name='ElectricalTest_HiPotential',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='inspection',
            name='ElectricalTest_PowerLED',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='inspection',
            name='ElectricalTest_PowerSWFunction',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='inspection',
            name='HardWare_Adjust',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='inspection',
            name='HardWare_Autoload',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='inspection',
            name='HardWare_BarcodeCarrier',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='inspection',
            name='HardWare_CalibrationTool',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='inspection',
            name='HardWare_Noise',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='inspection',
            name='HardWare_PIP_X1',
            field=models.IntegerField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='inspection',
            name='HardWare_PIP_X2',
            field=models.IntegerField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='inspection',
            name='HardWare_PIP_X3',
            field=models.IntegerField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='inspection',
            name='HardWare_PIP_X4',
            field=models.IntegerField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='inspection',
            name='HardWare_PIP_X5',
            field=models.IntegerField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='inspection',
            name='HardWare_PIP_X6',
            field=models.IntegerField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='inspection',
            name='HardWare_PIP_X7',
            field=models.IntegerField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='inspection',
            name='HardWare_PIP_X8',
            field=models.IntegerField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='inspection',
            name='HardWare_PIP_Y1',
            field=models.IntegerField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='inspection',
            name='HardWare_PIP_Y2',
            field=models.IntegerField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='inspection',
            name='HardWare_PIP_Y3',
            field=models.IntegerField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='inspection',
            name='HardWare_PIP_Y4',
            field=models.IntegerField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='inspection',
            name='HardWare_PIP_Y5',
            field=models.IntegerField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='inspection',
            name='HardWare_PIP_Y6',
            field=models.IntegerField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='inspection',
            name='HardWare_PIP_Y7',
            field=models.IntegerField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='inspection',
            name='HardWare_PIP_Y8',
            field=models.IntegerField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='inspection',
            name='HardWare_PIP_Z1',
            field=models.IntegerField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='inspection',
            name='HardWare_PIP_Z2',
            field=models.IntegerField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='inspection',
            name='HardWare_PIP_Z3',
            field=models.IntegerField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='inspection',
            name='HardWare_PIP_Z4',
            field=models.IntegerField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='inspection',
            name='HardWare_PIP_Z5',
            field=models.IntegerField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='inspection',
            name='HardWare_PIP_Z6',
            field=models.IntegerField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='inspection',
            name='HardWare_PIP_Z7',
            field=models.IntegerField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='inspection',
            name='HardWare_PIP_Z8',
            field=models.IntegerField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='inspection',
            name='HardWare_SN1',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='inspection',
            name='HardWare_SN2',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='inspection',
            name='HardWare_SN3',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='inspection',
            name='HardWare_SN4',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='inspection',
            name='HardWare_SN5',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='inspection',
            name='HardWare_SN6',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='inspection',
            name='HardWare_SN7',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='inspection',
            name='HardWare_SN8',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='inspection',
            name='HardWare_XArm_Diff',
            field=models.IntegerField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='inspection',
            name='HardWare_XArm_left',
            field=models.IntegerField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='inspection',
            name='HardWare_XArm_right',
            field=models.IntegerField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='inspection',
            name='HardWare_Xdev1',
            field=models.IntegerField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='inspection',
            name='HardWare_Xdev2',
            field=models.IntegerField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='inspection',
            name='HardWare_Xdev3',
            field=models.IntegerField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='inspection',
            name='HardWare_Xdev4',
            field=models.IntegerField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='inspection',
            name='HardWare_Xdev5',
            field=models.IntegerField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='inspection',
            name='HardWare_Xdev6',
            field=models.IntegerField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='inspection',
            name='HardWare_Xdev7',
            field=models.IntegerField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='inspection',
            name='HardWare_Xdev8',
            field=models.IntegerField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='inspection',
            name='HardWare_Xtilt1',
            field=models.IntegerField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='inspection',
            name='HardWare_Xtilt2',
            field=models.IntegerField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='inspection',
            name='HardWare_Xtilt3',
            field=models.IntegerField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='inspection',
            name='HardWare_Xtilt4',
            field=models.IntegerField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='inspection',
            name='HardWare_Xtilt5',
            field=models.IntegerField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='inspection',
            name='HardWare_Xtilt6',
            field=models.IntegerField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='inspection',
            name='HardWare_Xtilt7',
            field=models.IntegerField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='inspection',
            name='HardWare_Xtilt8',
            field=models.IntegerField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='inspection',
            name='HardWare_Ytilt1',
            field=models.IntegerField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='inspection',
            name='HardWare_Ytilt2',
            field=models.IntegerField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='inspection',
            name='HardWare_Ytilt3',
            field=models.IntegerField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='inspection',
            name='HardWare_Ytilt4',
            field=models.IntegerField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='inspection',
            name='HardWare_Ytilt5',
            field=models.IntegerField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='inspection',
            name='HardWare_Ytilt6',
            field=models.IntegerField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='inspection',
            name='HardWare_Ytilt7',
            field=models.IntegerField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='inspection',
            name='HardWare_Ytilt8',
            field=models.IntegerField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='inspection',
            name='Perfomance_Barcode',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='inspection',
            name='Perfomance_CoverSafety',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='inspection',
            name='Perfomance_HHS_RPM',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='inspection',
            name='Perfomance_HHS_SN',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='inspection',
            name='Perfomance_HHS_temperature',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='inspection',
            name='Perfomance_Loading_4mfxCarrier',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='inspection',
            name='Perfomance_Loading_TipCarrier',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='inspection',
            name='Perfomance_Loading_TubeCarrier',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='inspection',
            name='Perfomance_Loading_mtpCarrier',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='inspection',
            name='Perfomance_VFV_Accuracy1000ul1',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='inspection',
            name='Perfomance_VFV_Accuracy1000ul2',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='inspection',
            name='Perfomance_VFV_Accuracy1000ul3',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='inspection',
            name='Perfomance_VFV_Accuracy1000ul4',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='inspection',
            name='Perfomance_VFV_Accuracy1000ul5',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='inspection',
            name='Perfomance_VFV_Accuracy1000ul6',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='inspection',
            name='Perfomance_VFV_Accuracy1000ul7',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='inspection',
            name='Perfomance_VFV_Accuracy1000ul8',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='inspection',
            name='Perfomance_VFV_Accuracy300ul1',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='inspection',
            name='Perfomance_VFV_Accuracy300ul2',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='inspection',
            name='Perfomance_VFV_Accuracy300ul3',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='inspection',
            name='Perfomance_VFV_Accuracy300ul4',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='inspection',
            name='Perfomance_VFV_Accuracy300ul5',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='inspection',
            name='Perfomance_VFV_Accuracy300ul6',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='inspection',
            name='Perfomance_VFV_Accuracy300ul7',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='inspection',
            name='Perfomance_VFV_Accuracy300ul8',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='inspection',
            name='Perfomance_VFV_Precision1000ul1',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='inspection',
            name='Perfomance_VFV_Precision1000ul2',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='inspection',
            name='Perfomance_VFV_Precision1000ul3',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='inspection',
            name='Perfomance_VFV_Precision1000ul4',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='inspection',
            name='Perfomance_VFV_Precision1000ul5',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='inspection',
            name='Perfomance_VFV_Precision1000ul6',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='inspection',
            name='Perfomance_VFV_Precision1000ul7',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='inspection',
            name='Perfomance_VFV_Precision1000ul8',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='inspection',
            name='Perfomance_VFV_Precision300ul1',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='inspection',
            name='Perfomance_VFV_Precision300ul2',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='inspection',
            name='Perfomance_VFV_Precision300ul3',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='inspection',
            name='Perfomance_VFV_Precision300ul4',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='inspection',
            name='Perfomance_VFV_Precision300ul5',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='inspection',
            name='Perfomance_VFV_Precision300ul6',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='inspection',
            name='Perfomance_VFV_Precision300ul7',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='inspection',
            name='Perfomance_VFV_Precision300ul8',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='inspection',
            name='Perfomance_XYZpositioning',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='Instrument_SN',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Instrumentapp.instrument'),
        ),
    ]
