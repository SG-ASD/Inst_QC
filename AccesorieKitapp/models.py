from django.db import models

from Instrumentapp.models import Instrument


class Accessories(models.Model):
    Instrument_SN = models.ForeignKey(Instrument, on_delete=models.CASCADE, db_column='Instrument_SN', related_name='Acc_Instrument_SN')  # 시리얼번호
    Unpack_Instructions = models.CharField(max_length=20, null=True, blank=True)
    Installation_Qualification = models.CharField(max_length=20, null=True, blank=True)
    Final_Configuation = models.CharField(max_length=20, null=True, blank=True)
    Measurement_Protocol = models.CharField(max_length=20, null=True, blank=True)
    EU_Declaration = models.CharField(max_length=20, null=True, blank=True)
    DeclarationSTARlet = models.CharField(max_length=20, null=True, blank=True)
    Declaration_Quality = models.CharField(max_length=20, null=True, blank=True)
    Packing_Checklist = models.CharField(max_length=20, null=True, blank=True)
    Maintenance = models.CharField(max_length=20, null=True, blank=True)
    Channel_Adjust = models.CharField(max_length=20, null=True, blank=True)
    Test_Report = models.CharField(max_length=20, null=True, blank=True)
    Loading_Table = models.CharField(max_length=20, null=True, blank=True)
    Side_Cover_right = models.CharField(max_length=20, null=True, blank=True)
    Side_Cover_left = models.CharField(max_length=20, null=True, blank=True)
    Rear_Piexiglas = models.CharField(max_length=20, null=True, blank=True)
    Top_Plexiglas = models.CharField(max_length=20, null=True, blank=True)
    Left_Plexiglas = models.CharField(max_length=20, null=True, blank=True)
    Right_Plexiglas = models.CharField(max_length=20, null=True, blank=True)

    Sensor_4L = models.CharField(max_length=20, null=True, blank=True)
    Solid_Waste = models.CharField(max_length=20, null=True, blank=True)
    USB_Liquid = models.CharField(max_length=20, null=True, blank=True)
    USB_Solid_Liquid = models.CharField(max_length=20, null=True, blank=True)
    USB_Venus = models.CharField(max_length=20, null=True, blank=True)
    Eppendorf = models.CharField(max_length=20, null=True, blank=True)
    Core_Gripper = models.CharField(max_length=20, null=True, blank=True)
    Needle_Check = models.CharField(max_length=20, null=True, blank=True)
    Needle_Lot = models.CharField(max_length=20, null=True, blank=True)
    Separator = models.CharField(max_length=20, null=True, blank=True)
    Tip_Eject = models.CharField(max_length=20, null=True, blank=True)
    Power_Cord7 = models.CharField(max_length=20, null=True, blank=True)
    Power_CordP = models.CharField(max_length=20, null=True, blank=True)
    Cable_USB = models.CharField(max_length=20, null=True, blank=True)
    Fuse = models.CharField(max_length=20, null=True, blank=True)
    Screw = models.CharField(max_length=20, null=True, blank=True)
    Fitting = models.CharField(max_length=20, null=True, blank=True)
    Liq_Waste = models.CharField(max_length=20, null=True, blank=True)

    XArm = models.CharField(max_length=20, null=True, blank=True)
    Bar_Left = models.CharField(max_length=20, null=True, blank=True)
    Bar_Top = models.CharField(max_length=20, null=True, blank=True)

    Bag = models.CharField(max_length=20, null=True, blank=True)
    Tube_32 = models.CharField(max_length=20, null=True, blank=True)
    TipRack_5 = models.CharField(max_length=20, null=True, blank=True)
    MFX4 = models.CharField(max_length=20, null=True, blank=True)
    SEEG = models.CharField(max_length=20, null=True, blank=True)
    FLHX = models.CharField(max_length=20, null=True, blank=True)
    SOHX = models.CharField(max_length=20, null=True, blank=True)
    HHS_Plate = models.CharField(max_length=20, null=True, blank=True)
    MTP = models.CharField(max_length=20, null=True, blank=True)
    Verify_Kit = models.CharField(max_length=20, null=True, blank=True)
    STD = models.CharField(max_length=20, null=True, blank=True)
    High = models.CharField(max_length=20, null=True, blank=True)
    HHS_SN = models.CharField(max_length=20, null=True, blank=True)
    HHS_Check = models.CharField(max_length=20, null=True, blank=True)
    HHS_Manual = models.CharField(max_length=20, null=True, blank=True)
    Stop_Barcode = models.CharField(max_length=20, null=True, blank=True)
    Remark = models.CharField(max_length=200, null=True, blank=True)


class AccessoriesFiles(models.Model):
    Instrument_SN = models.ForeignKey(Instrument, on_delete=models.CASCADE, db_column='Instrument_SN', related_name='AccFile_Instrument_SN')  # 시리얼번호
    Unpack_Instructions_Files = models.TextField(blank=True)
    Installation_Qualification_Files = models.TextField(blank=True)
    Final_Configuation_Files = models.TextField(blank=True)
    Measurement_Protocol_Files = models.TextField(blank=True)
    EU_Declaration_Files = models.TextField(blank=True)
    DeclarationSTARlet_Files = models.TextField(blank=True)
    Declaration_Quality_Files = models.TextField(blank=True)
    Packing_Checklist_Files = models.TextField(blank=True)
    Maintenance_Files = models.TextField(blank=True)
    Channel_Adjust_Files = models.TextField(blank=True)
    Test_Report_Files = models.TextField(blank=True)
    Loading_Table_Files = models.TextField(blank=True)
    Side_Cover_right_Files = models.TextField(blank=True)
    Side_Cover_left_Files = models.TextField(blank=True)
    Rear_Piexiglas_Files = models.TextField(blank=True)
    Top_Plexiglas_Files = models.TextField(blank=True)
    Left_Plexiglas_Files = models.TextField(blank=True)
    Right_Plexiglas_Files = models.TextField(blank=True)

    Sensor_4L_Files = models.TextField(blank=True)
    Solid_Waste_Files = models.TextField(blank=True)
    USB_Liquid_Files = models.TextField(blank=True)
    USB_Solid_Liquid_Files = models.TextField(blank=True)
    USB_Venus_Files = models.TextField(blank=True)
    Eppendorf_Files = models.TextField(blank=True)
    Core_Gripper_Files = models.TextField(blank=True)
    Needle_Check_Files = models.TextField(blank=True)
    Separator_Files = models.TextField(blank=True)
    Tip_Eject_Files = models.TextField(blank=True)
    Power_Cord7_Files = models.TextField(blank=True)
    Power_CordP_Files = models.TextField(blank=True)
    Cable_USB_Files = models.TextField(blank=True)
    Fuse_Files = models.TextField(blank=True)
    Screw_Files = models.TextField(blank=True)
    Fitting_Files = models.TextField(blank=True)
    Liq_Waste_Files = models.TextField(blank=True)

    XArm_Files = models.TextField(blank=True)
    Bar_Left_Files = models.TextField(blank=True)
    Bar_Top_Files = models.TextField(blank=True)

    Bag_Files = models.TextField(blank=True)
    Tube_32_Files = models.TextField(blank=True)
    TipRack_5_Files = models.TextField(blank=True)
    MFX4_Files = models.TextField(blank=True)
    SEEG_Files = models.TextField(blank=True)
    FLHX_Files = models.TextField(blank=True)
    SOHX_Files = models.TextField(blank=True)
    HHS_Plate_Files = models.TextField(blank=True)
    MTP_Files = models.TextField(blank=True)
    Verify_Kit_Files = models.TextField(blank=True)
    STD_Files = models.TextField(blank=True)
    High_Files = models.TextField(blank=True)
    HHS_Check_Files = models.TextField(blank=True)
    HHS_Manual_Files = models.TextField(blank=True)
    Stop_Barcode_Files = models.TextField(blank=True)
    Remark_Files = models.TextField(blank=True)

    def __str__(self):
        return self.Instrument_SN_id
