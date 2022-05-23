# Generated by Django 4.0.3 on 2022-05-19 02:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Instrumentapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accessories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Unpack_Instructions', models.CharField(blank=True, max_length=20)),
                ('Installation_Qualification', models.CharField(blank=True, max_length=20)),
                ('Final_Configuation', models.CharField(blank=True, max_length=20)),
                ('Measurement_Protocol', models.CharField(blank=True, max_length=20)),
                ('DeclarationSTARlet', models.CharField(blank=True, max_length=20)),
                ('MeasurementProtocolSTARlet', models.CharField(blank=True, max_length=20)),
                ('EU_Declaration', models.CharField(blank=True, max_length=20)),
                ('Declaration_Quality', models.CharField(blank=True, max_length=20)),
                ('Packing_Checklist', models.CharField(blank=True, max_length=20)),
                ('Maintenance', models.CharField(blank=True, max_length=20)),
                ('Channel_Adjust', models.CharField(blank=True, max_length=20)),
                ('Test_Report', models.CharField(blank=True, max_length=20)),
                ('Loading_Table', models.CharField(blank=True, max_length=20)),
                ('Side_Cover_right', models.CharField(blank=True, max_length=20)),
                ('Side_Cover_left', models.CharField(blank=True, max_length=20)),
                ('Rear_Piexiglas', models.CharField(blank=True, max_length=20)),
                ('Left_Plexiglas', models.CharField(blank=True, max_length=20)),
                ('Right_Plexiglas', models.CharField(blank=True, max_length=20)),
                ('Top_Plexiglas', models.CharField(blank=True, max_length=20)),
                ('Sensor_4L', models.CharField(blank=True, max_length=20)),
                ('Solid_Waste', models.CharField(blank=True, max_length=20)),
                ('USB_Liquid', models.CharField(blank=True, max_length=20)),
                ('USB_Solid_Liquid', models.CharField(blank=True, max_length=20)),
                ('USB_Venus', models.CharField(blank=True, max_length=20)),
                ('Eppendorf', models.CharField(blank=True, max_length=20)),
                ('Core_Gripper', models.CharField(blank=True, max_length=20)),
                ('Needle_Check', models.CharField(blank=True, max_length=20)),
                ('Needle_Lot', models.CharField(blank=True, max_length=20)),
                ('Separator', models.CharField(blank=True, max_length=20)),
                ('Tip_Eject', models.CharField(blank=True, max_length=20)),
                ('Power_Cord7', models.CharField(blank=True, max_length=20)),
                ('Power_CordP', models.CharField(blank=True, max_length=20)),
                ('Cable_USB', models.CharField(blank=True, max_length=20)),
                ('Fuse', models.CharField(blank=True, max_length=20)),
                ('Screw', models.CharField(blank=True, max_length=20)),
                ('Fitting', models.CharField(blank=True, max_length=20)),
                ('Liq_Waste', models.CharField(blank=True, max_length=20)),
                ('XArm', models.CharField(blank=True, max_length=20)),
                ('Bar_Left', models.CharField(blank=True, max_length=20)),
                ('Bar_Top', models.CharField(blank=True, max_length=20)),
                ('Bag', models.CharField(blank=True, max_length=20)),
                ('Tube_32', models.CharField(blank=True, max_length=20)),
                ('TipRack_5', models.CharField(blank=True, max_length=20)),
                ('MFX4', models.CharField(blank=True, max_length=20)),
                ('SEEG', models.CharField(blank=True, max_length=20)),
                ('FLHX', models.CharField(blank=True, max_length=20)),
                ('SOHX', models.CharField(blank=True, max_length=20)),
                ('HHS_Plate', models.CharField(blank=True, max_length=20)),
                ('MTP', models.CharField(blank=True, max_length=20)),
                ('Verify_Kit', models.CharField(blank=True, max_length=20)),
                ('STD', models.CharField(blank=True, max_length=20)),
                ('High', models.CharField(blank=True, max_length=20)),
                ('HHS_SN', models.CharField(blank=True, max_length=20)),
                ('HHS_Check', models.CharField(blank=True, max_length=20)),
                ('HHS_Manual', models.CharField(blank=True, max_length=20)),
                ('Stop_Barcode', models.CharField(blank=True, max_length=20)),
                ('Instrument_SN', models.ForeignKey(db_column='Instrument_SN', on_delete=django.db.models.deletion.CASCADE, related_name='Acc_Instrument_SN', to='Instrumentapp.instrument')),
            ],
        ),
    ]