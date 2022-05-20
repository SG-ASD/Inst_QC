from django.db import models

from Instrumentapp.models import Instrument


class Accessories(models.Model):
    Instrument_SN = models.ForeignKey(Instrument, on_delete=models.CASCADE, db_column='Instrument_SN', related_name='Acc_Instrument_SN')  # 관리번호
    Unpack_Instructions = models.CharField(max_length=20, blank=True)  # 시리얼번호
    Installation_Qualification = models.CharField(max_length=20, blank=True)  # 장비명
    Final_Configuation = models.CharField(max_length=20, blank=True)  # 설비 및 계측기
    Measurement_Protocol = models.CharField(max_length=20, blank=True)  # 설비 및 계측기
    DeclarationSTARlet = models.CharField(max_length=20, blank=True)  # 설비 및 계측기
    EU_Declaration = models.CharField(max_length=20, blank=True)  # 설비 및 계측기
    Declaration_Quality = models.CharField(max_length=20, blank=True)  # 설비 및 계측기
    Packing_Checklist = models.CharField(max_length=20, blank=True)  # 설비 및 계측기
    Maintenance = models.CharField(max_length=20, blank=True)  # 설비 및 계측기
    Channel_Adjust = models.CharField(max_length=20, blank=True)  # 설비 및 계측기
    Test_Report = models.CharField(max_length=20, blank=True)  # 설비 및 계측기
    Loading_Table = models.CharField(max_length=20, blank=True)  # 설비 및 계측기
    Side_Cover_right = models.CharField(max_length=20, blank=True)  # 설비 및 계측기
    Side_Cover_left = models.CharField(max_length=20, blank=True)  # 설비 및 계측기
    Rear_Piexiglas = models.CharField(max_length=20, blank=True)  # 설비 및 계측기
    Left_Plexiglas = models.CharField(max_length=20, blank=True)  # 설비 및 계측기
    Right_Plexiglas = models.CharField(max_length=20, blank=True)  # 설비 및 계측기
    Top_Plexiglas = models.CharField(max_length=20, blank=True)  # 설비 및 계측기

    Sensor_4L = models.CharField(max_length=20, blank=True)  # 설비 및 계측기
    Solid_Waste = models.CharField(max_length=20, blank=True)  # 설비 및 계측기
    USB_Liquid = models.CharField(max_length=20, blank=True)  # 설비 및 계측기
    USB_Solid_Liquid = models.CharField(max_length=20, blank=True)  # 설비 및 계측기
    USB_Venus = models.CharField(max_length=20, blank=True)  # 설비 및 계측기
    Eppendorf = models.CharField(max_length=20, blank=True)  # 설비 및 계측기
    Core_Gripper = models.CharField(max_length=20, blank=True)  # 설비 및 계측기
    Needle_Check = models.CharField(max_length=20, blank=True)  # 설비 및 계측기
    Needle_Lot = models.CharField(max_length=20, blank=True)  # 설비 및 계측기
    Separator = models.CharField(max_length=20, blank=True)  # 설비 및 계측기
    Tip_Eject = models.CharField(max_length=20, blank=True)  # 설비 및 계측기
    Power_Cord7 = models.CharField(max_length=20, blank=True)  # 설비 및 계측기
    Power_CordP = models.CharField(max_length=20, blank=True)  # 설비 및 계측기
    Cable_USB = models.CharField(max_length=20, blank=True)  # 설비 및 계측기
    Fuse = models.CharField(max_length=20, blank=True)  # 설비 및 계측기
    Screw = models.CharField(max_length=20, blank=True)  # 설비 및 계측기
    Fitting = models.CharField(max_length=20, blank=True)  # 설비 및 계측기
    Liq_Waste = models.CharField(max_length=20, blank=True)  # 설비 및 계측기

    XArm = models.CharField(max_length=20, blank=True)  # 설비 및 계측기
    Bar_Left = models.CharField(max_length=20, blank=True)  # 설비 및 계측기
    Bar_Top = models.CharField(max_length=20, blank=True)  # 설비 및 계측기
    Bag = models.CharField(max_length=20, blank=True)  # 설비 및 계측기
    Tube_32 = models.CharField(max_length=20, blank=True)  # 설비 및 계측기
    TipRack_5 = models.CharField(max_length=20, blank=True)  # 설비 및 계측기
    MFX4 = models.CharField(max_length=20, blank=True)  # 설비 및 계측기
    SEEG = models.CharField(max_length=20, blank=True)  # 설비 및 계측기
    FLHX = models.CharField(max_length=20, blank=True)  # 설비 및 계측기
    SOHX = models.CharField(max_length=20, blank=True)  # 설비 및 계측기
    HHS_Plate = models.CharField(max_length=20, blank=True)  # 설비 및 계측기
    MTP = models.CharField(max_length=20, blank=True)  # 설비 및 계측기
    Verify_Kit = models.CharField(max_length=20, blank=True)  # 설비 및 계측기
    STD = models.CharField(max_length=20, blank=True)  # 설비 및 계측기
    High = models.CharField(max_length=20, blank=True)  # 설비 및 계측기
    HHS_SN = models.CharField(max_length=20, blank=True)  # 설비 및 계측기
    HHS_Check = models.CharField(max_length=20, blank=True)  # 설비 및 계측기
    HHS_Manual = models.CharField(max_length=20, blank=True)  # 설비 및 계측기
    Stop_Barcode = models.CharField(max_length=20, blank=True)  # 설비 및 계측기
    Remark = models.CharField(max_length=200, blank=True)  # 설비 및 계측기
