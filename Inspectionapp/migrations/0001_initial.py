# Generated by Django 3.2.5 on 2022-07-20 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Instrumentapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inspection',
            fields=[
                ('Instrument_SN', models.OneToOneField(db_column='Instrument_SN', on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='Inspection', serialize=False, to='Instrumentapp.instrument')),
                ('Name', models.TextField(blank=True, max_length=60)),
                ('Inspector', models.TextField(blank=True, max_length=20)),
                ('Start_Date', models.DateField(blank=True, null=True)),
                ('CompleteDt', models.DateField(blank=True, null=True)),
                ('Status', models.TextField(blank=True, max_length=20)),
                ('Revision', models.TextField(blank=True, max_length=50)),
                ('SW_Version', models.TextField(blank=True, max_length=50)),
                ('FV2_Version', models.TextField(blank=True, max_length=50)),
                ('FW_PipetteCh', models.TextField(blank=True, max_length=50)),
                ('FW_Xdrive', models.TextField(blank=True, max_length=50)),
                ('FW_Master', models.TextField(blank=True, max_length=50)),
                ('Computer_SN', models.TextField(blank=True, max_length=50)),
                ('Appearance_Shock_Watch', models.TextField(blank=True, max_length=20)),
                ('Appearance_Binding', models.TextField(blank=True, max_length=20)),
                ('Appearance_Labels', models.TextField(blank=True, max_length=20)),
                ('Appearance_Packaging_Box', models.TextField(blank=True, max_length=20)),
                ('Appearance_Wooden_Pallet', models.TextField(blank=True, max_length=20)),
                ('Appearance_Transport_Jig', models.TextField(blank=True, max_length=20)),
                ('Appearance_Shock_Watch_Image', models.TextField(blank=True)),
                ('Appearance_Binding_Image', models.TextField(blank=True)),
                ('Appearance_Labels_Image', models.TextField(blank=True)),
                ('Appearance_Packaging_Box_Image', models.TextField(blank=True)),
                ('Appearance_Wooden_Pallet_Image', models.TextField(blank=True)),
                ('Appearance_Transport_Jig_Image', models.TextField(blank=True)),
                ('Appearance_Video', models.TextField(blank=True)),
                ('Appearance_Front', models.TextField(blank=True, max_length=20)),
                ('Appearance_Top', models.TextField(blank=True, max_length=20)),
                ('Appearance_Right', models.TextField(blank=True, max_length=20)),
                ('Appearance_Left', models.TextField(blank=True, max_length=20)),
                ('Appearance_Back', models.TextField(blank=True, max_length=20)),
                ('Appearance_Acc_Damage', models.TextField(blank=True, max_length=20)),
                ('Appearance_Acc_Missing', models.TextField(blank=True, max_length=20)),
                ('ElectricalTest_HiPotential', models.TextField(blank=True, max_length=20)),
                ('ElectricalTest_GroundResistance', models.TextField(blank=True, max_length=20)),
                ('ElectricalTest_PowerSWFunction', models.TextField(blank=True, max_length=20)),
                ('ElectricalTest_PowerLED', models.TextField(blank=True, max_length=20)),
                ('HardWare_CalibrationTool', models.TextField(blank=True, max_length=20)),
                ('HardWare_BarcodeCarrier', models.TextField(blank=True, max_length=20)),
                ('HardWare_XArm_left', models.IntegerField(blank=True, null=True)),
                ('HardWare_XArm_right', models.IntegerField(blank=True, null=True)),
                ('HardWare_XArm_Diff', models.IntegerField(blank=True, null=True)),
                ('HardWare_Autoload', models.TextField(blank=True, max_length=20)),
                ('HardWare_Noise', models.TextField(blank=True, max_length=20)),
                ('HardWare_Xdev1', models.IntegerField(blank=True, null=True)),
                ('HardWare_Xdev2', models.IntegerField(blank=True, null=True)),
                ('HardWare_Xdev3', models.IntegerField(blank=True, null=True)),
                ('HardWare_Xdev4', models.IntegerField(blank=True, null=True)),
                ('HardWare_Xdev5', models.IntegerField(blank=True, null=True)),
                ('HardWare_Xdev6', models.IntegerField(blank=True, null=True)),
                ('HardWare_Xdev7', models.IntegerField(blank=True, null=True)),
                ('HardWare_Xdev8', models.IntegerField(blank=True, null=True)),
                ('HardWare_Xtilt1', models.IntegerField(blank=True, null=True)),
                ('HardWare_Xtilt2', models.IntegerField(blank=True, null=True)),
                ('HardWare_Xtilt3', models.IntegerField(blank=True, null=True)),
                ('HardWare_Xtilt4', models.IntegerField(blank=True, null=True)),
                ('HardWare_Xtilt5', models.IntegerField(blank=True, null=True)),
                ('HardWare_Xtilt6', models.IntegerField(blank=True, null=True)),
                ('HardWare_Xtilt7', models.IntegerField(blank=True, null=True)),
                ('HardWare_Xtilt8', models.IntegerField(blank=True, null=True)),
                ('HardWare_Ytilt1', models.IntegerField(blank=True, null=True)),
                ('HardWare_Ytilt2', models.IntegerField(blank=True, null=True)),
                ('HardWare_Ytilt3', models.IntegerField(blank=True, null=True)),
                ('HardWare_Ytilt4', models.IntegerField(blank=True, null=True)),
                ('HardWare_Ytilt5', models.IntegerField(blank=True, null=True)),
                ('HardWare_Ytilt6', models.IntegerField(blank=True, null=True)),
                ('HardWare_Ytilt7', models.IntegerField(blank=True, null=True)),
                ('HardWare_Ytilt8', models.IntegerField(blank=True, null=True)),
                ('HardWare_SN1', models.TextField(blank=True, max_length=20)),
                ('HardWare_SN2', models.TextField(blank=True, max_length=20)),
                ('HardWare_SN3', models.TextField(blank=True, max_length=20)),
                ('HardWare_SN4', models.TextField(blank=True, max_length=20)),
                ('HardWare_SN5', models.TextField(blank=True, max_length=20)),
                ('HardWare_SN6', models.TextField(blank=True, max_length=20)),
                ('HardWare_SN7', models.TextField(blank=True, max_length=20)),
                ('HardWare_SN8', models.TextField(blank=True, max_length=20)),
                ('HardWare_Adjust', models.TextField(blank=True, max_length=20)),
                ('HardWare_PIP_X1', models.IntegerField(blank=True, default=0, null=True)),
                ('HardWare_PIP_X2', models.IntegerField(blank=True, default=0, null=True)),
                ('HardWare_PIP_X3', models.IntegerField(blank=True, default=0, null=True)),
                ('HardWare_PIP_X4', models.IntegerField(blank=True, default=0, null=True)),
                ('HardWare_PIP_X5', models.IntegerField(blank=True, default=0, null=True)),
                ('HardWare_PIP_X6', models.IntegerField(blank=True, default=0, null=True)),
                ('HardWare_PIP_X7', models.IntegerField(blank=True, default=0, null=True)),
                ('HardWare_PIP_X8', models.IntegerField(blank=True, default=0, null=True)),
                ('HardWare_PIP_Y1', models.IntegerField(blank=True, default=0, null=True)),
                ('HardWare_PIP_Y2', models.IntegerField(blank=True, default=0, null=True)),
                ('HardWare_PIP_Y3', models.IntegerField(blank=True, default=0, null=True)),
                ('HardWare_PIP_Y4', models.IntegerField(blank=True, default=0, null=True)),
                ('HardWare_PIP_Y5', models.IntegerField(blank=True, default=0, null=True)),
                ('HardWare_PIP_Y6', models.IntegerField(blank=True, default=0, null=True)),
                ('HardWare_PIP_Y7', models.IntegerField(blank=True, default=0, null=True)),
                ('HardWare_PIP_Y8', models.IntegerField(blank=True, default=0, null=True)),
                ('HardWare_PIP_Z1', models.IntegerField(blank=True, default=0, null=True)),
                ('HardWare_PIP_Z2', models.IntegerField(blank=True, default=0, null=True)),
                ('HardWare_PIP_Z3', models.IntegerField(blank=True, default=0, null=True)),
                ('HardWare_PIP_Z4', models.IntegerField(blank=True, default=0, null=True)),
                ('HardWare_PIP_Z5', models.IntegerField(blank=True, default=0, null=True)),
                ('HardWare_PIP_Z6', models.IntegerField(blank=True, default=0, null=True)),
                ('HardWare_PIP_Z7', models.IntegerField(blank=True, default=0, null=True)),
                ('HardWare_PIP_Z8', models.IntegerField(blank=True, default=0, null=True)),
                ('Perfomance_CoverSafety', models.TextField(blank=True, max_length=20)),
                ('Perfomance_Barcode', models.TextField(blank=True, max_length=20)),
                ('Perfomance_XYZpositioning', models.TextField(blank=True, max_length=20)),
                ('Perfomance_HHS_SN', models.TextField(blank=True, max_length=20)),
                ('Perfomance_HHS_temperature', models.TextField(blank=True, max_length=20)),
                ('Perfomance_HHS_RPM', models.TextField(blank=True, max_length=20)),
                ('Perfomance_Loading_TipCarrier', models.TextField(blank=True, max_length=20)),
                ('Perfomance_Loading_TubeCarrier', models.TextField(blank=True, max_length=20)),
                ('Perfomance_Loading_mtpCarrier', models.TextField(blank=True, max_length=20)),
                ('Perfomance_Loading_4mfxCarrier', models.TextField(blank=True, max_length=20)),
                ('Perfomance_VFV_Accuracy300ul1', models.TextField(blank=True, max_length=20)),
                ('Perfomance_VFV_Accuracy300ul2', models.TextField(blank=True, max_length=20)),
                ('Perfomance_VFV_Accuracy300ul3', models.TextField(blank=True, max_length=20)),
                ('Perfomance_VFV_Accuracy300ul4', models.TextField(blank=True, max_length=20)),
                ('Perfomance_VFV_Accuracy300ul5', models.TextField(blank=True, max_length=20)),
                ('Perfomance_VFV_Accuracy300ul6', models.TextField(blank=True, max_length=20)),
                ('Perfomance_VFV_Accuracy300ul7', models.TextField(blank=True, max_length=20)),
                ('Perfomance_VFV_Accuracy300ul8', models.TextField(blank=True, max_length=20)),
                ('Perfomance_VFV_Precision300ul1', models.TextField(blank=True, max_length=20)),
                ('Perfomance_VFV_Precision300ul2', models.TextField(blank=True, max_length=20)),
                ('Perfomance_VFV_Precision300ul3', models.TextField(blank=True, max_length=20)),
                ('Perfomance_VFV_Precision300ul4', models.TextField(blank=True, max_length=20)),
                ('Perfomance_VFV_Precision300ul5', models.TextField(blank=True, max_length=20)),
                ('Perfomance_VFV_Precision300ul6', models.TextField(blank=True, max_length=20)),
                ('Perfomance_VFV_Precision300ul7', models.TextField(blank=True, max_length=20)),
                ('Perfomance_VFV_Precision300ul8', models.TextField(blank=True, max_length=20)),
                ('Perfomance_VFV_Accuracy1000ul1', models.TextField(blank=True, max_length=20)),
                ('Perfomance_VFV_Accuracy1000ul2', models.TextField(blank=True, max_length=20)),
                ('Perfomance_VFV_Accuracy1000ul3', models.TextField(blank=True, max_length=20)),
                ('Perfomance_VFV_Accuracy1000ul4', models.TextField(blank=True, max_length=20)),
                ('Perfomance_VFV_Accuracy1000ul5', models.TextField(blank=True, max_length=20)),
                ('Perfomance_VFV_Accuracy1000ul6', models.TextField(blank=True, max_length=20)),
                ('Perfomance_VFV_Accuracy1000ul7', models.TextField(blank=True, max_length=20)),
                ('Perfomance_VFV_Accuracy1000ul8', models.TextField(blank=True, max_length=20)),
                ('Perfomance_VFV_Precision1000ul1', models.TextField(blank=True, max_length=20)),
                ('Perfomance_VFV_Precision1000ul2', models.TextField(blank=True, max_length=20)),
                ('Perfomance_VFV_Precision1000ul3', models.TextField(blank=True, max_length=20)),
                ('Perfomance_VFV_Precision1000ul4', models.TextField(blank=True, max_length=20)),
                ('Perfomance_VFV_Precision1000ul5', models.TextField(blank=True, max_length=20)),
                ('Perfomance_VFV_Precision1000ul6', models.TextField(blank=True, max_length=20)),
                ('Perfomance_VFV_Precision1000ul7', models.TextField(blank=True, max_length=20)),
                ('Perfomance_VFV_Precision1000ul8', models.TextField(blank=True, max_length=20)),
                ('Attachment_CoverSafety_Report', models.TextField(blank=True, max_length=20)),
                ('Attachment_Barcode_Report', models.TextField(blank=True, max_length=20)),
                ('Attachment_Position_Report', models.TextField(blank=True, max_length=20)),
                ('Attachment_Declaration_HHS', models.TextField(blank=True, max_length=20)),
                ('Attachment_Declaration', models.TextField(blank=True, max_length=20)),
                ('Attachment_Measurement_Protocol', models.TextField(blank=True, max_length=20)),
                ('Attachment_ElectricalSafety_Report', models.TextField(blank=True, max_length=20)),
                ('Attachment_CoverSafety_Report_File', models.TextField(blank=True)),
                ('Attachment_Barcode_Report_File', models.TextField(blank=True)),
                ('Attachment_Position_Report_File', models.TextField(blank=True)),
                ('Attachment_Files', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Inspection_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category', models.CharField(max_length=30)),
                ('Subcategory', models.CharField(max_length=60)),
            ],
        ),
    ]
