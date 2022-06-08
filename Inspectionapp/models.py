import os
from django.contrib.auth.models import User
from django.db import models
from Instrumentapp.models import Instrument
from django.urls import resolve
# Create your models here.
from django.http import request


class Inspection(models.Model):
    # 1:1 매칭 시켜준다. User 와 Profile 1:! 매칭
    # related_name = request.user.profile.nickname
    # user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    def Attachment_image_path(instance, filename):
        # MEDEIA_ROOT/user_<pk>/ 경로로 <filename> 이름으로 업로드
        return f'{instance.Instrument_SN_id}/{filename}'

    def Appearance_image_path(instance, filename):
        # MEDEIA_ROOT/user_<pk>/ 경로로 <filename> 이름으로 업로드
        filename = "ShockWatch.jpg"
        return f'{instance.Instrument_SN_id}/{filename}'

    def test_path(instance, filename):
        print("test_path")
        print(f"filename:{filename}")
        filename = "test_image.jpg"
        print(f"type:{type(instance)}")
        print(f"instance.Instrument_SN_id:{instance.Instrument_SN_id}")
        return f'{instance.Instrument_SN_id}/{filename}'

    # Inspection
    Instrument_SN = models.OneToOneField(Instrument, on_delete=models.CASCADE, db_column='Instrument_SN', related_name='Inspection', primary_key=True, unique=True)  # 장비 SN
    Name = models.CharField(max_length=60, blank=True)  # 장비명
    Inspector = models.CharField(max_length=20, blank=True)  # 검사자
    Start_Date = models.DateField(null=True, blank=True)  # 검사시작일
    Completed_Date = models.DateField(null=True, blank=True)  # 검사완료일
    Status = models.CharField(max_length=20, blank=True)  # 검사 상태
    Revision = models.CharField(max_length=50, blank=True)  # 검사성적서 Revision
    SW_Version = models.CharField(max_length=50, blank=True)  # SW 버전
    FV2_Version = models.CharField(max_length=50, blank=True)  # FV2 버전
    FW_PipetteCh = models.CharField(max_length=50, blank=True)  # PipetteCh 버전
    FW_Xdrive = models.CharField(max_length=50, blank=True)  # X-drive 버전
    FW_Master = models.CharField(max_length=50, blank=True)  # Master 버전
    Computer_SN = models.CharField(max_length=50, blank=True)  # 컴퓨터 SN

    # 1.Appearance
    Appearance_Shock_Watch = models.CharField(max_length=20, blank=True)
    Appearance_Binding = models.CharField(max_length=20, blank=True)
    Appearance_Labels = models.CharField(max_length=20, blank=True)
    Appearance_Packaging_Box = models.CharField(max_length=20, blank=True)
    Appearance_Wooden_Pallet = models.CharField(max_length=20, blank=True)
    Appearance_Transport_Jig = models.CharField(max_length=20, blank=True)

    Appearance_Shock_Watch_Image = models.ImageField(upload_to=test_path, blank=True)
    Appearance_Binding_Image = models.ImageField(upload_to=Appearance_image_path, blank=True)
    Appearance_Labels_Image = models.ImageField(upload_to=Appearance_image_path, blank=True)
    Appearance_Packaging_Box_Image = models.ImageField(upload_to=Appearance_image_path, blank=True)
    Appearance_Wooden_Pallet_Image = models.ImageField(upload_to=Appearance_image_path, blank=True)
    Appearance_Transport_Jig_Image = models.ImageField(upload_to=Appearance_image_path, blank=True)
    Appearance_Video = models.FileField(upload_to=Appearance_image_path, blank=True)

    Appearance_Front = models.CharField(max_length=20, blank=True)
    Appearance_Top = models.CharField(max_length=20, blank=True)
    Appearance_Right = models.CharField(max_length=20, blank=True)
    Appearance_Left = models.CharField(max_length=20, blank=True)
    Appearance_Back = models.CharField(max_length=20, blank=True)
    Appearance_Acc_Damage = models.CharField(max_length=20, blank=True)
    Appearance_Acc_Missing = models.CharField(max_length=20, blank=True)

    # 2.ElectricalTest
    ElectricalTest_HiPotential = models.CharField(max_length=20, blank=True)
    ElectricalTest_GroundResistance = models.CharField(max_length=20, blank=True)
    ElectricalTest_PowerSWFunction = models.CharField(max_length=20, blank=True)
    ElectricalTest_PowerLED = models.CharField(max_length=20, blank=True)

    # 3.HardWare
    HardWare_CalibrationTool = models.CharField(max_length=20, blank=True)
    HardWare_BarcodeCarrier = models.CharField(max_length=20, blank=True)
    HardWare_XArm_left = models.IntegerField(null=True, blank=True)
    HardWare_XArm_right = models.IntegerField(null=True, blank=True)
    HardWare_XArm_Diff = models.IntegerField(null=True, blank=True)
    HardWare_Autoload = models.CharField(max_length=20, blank=True)
    HardWare_Noise = models.CharField(max_length=20, blank=True)
    HardWare_Xdev1 = models.IntegerField(null=True, blank=True)
    HardWare_Xdev2 = models.IntegerField(null=True, blank=True)
    HardWare_Xdev3 = models.IntegerField(null=True, blank=True)
    HardWare_Xdev4 = models.IntegerField(null=True, blank=True)
    HardWare_Xdev5 = models.IntegerField(null=True, blank=True)
    HardWare_Xdev6 = models.IntegerField(null=True, blank=True)
    HardWare_Xdev7 = models.IntegerField(null=True, blank=True)
    HardWare_Xdev8 = models.IntegerField(null=True, blank=True)
    HardWare_Xtilt1 = models.IntegerField(null=True, blank=True)
    HardWare_Xtilt2 = models.IntegerField(null=True, blank=True)
    HardWare_Xtilt3 = models.IntegerField(null=True, blank=True)
    HardWare_Xtilt4 = models.IntegerField(null=True, blank=True)
    HardWare_Xtilt5 = models.IntegerField(null=True, blank=True)
    HardWare_Xtilt6 = models.IntegerField(null=True, blank=True)
    HardWare_Xtilt7 = models.IntegerField(null=True, blank=True)
    HardWare_Xtilt8 = models.IntegerField(null=True, blank=True)
    HardWare_Ytilt1 = models.IntegerField(null=True, blank=True)
    HardWare_Ytilt2 = models.IntegerField(null=True, blank=True)
    HardWare_Ytilt3 = models.IntegerField(null=True, blank=True)
    HardWare_Ytilt4 = models.IntegerField(null=True, blank=True)
    HardWare_Ytilt5 = models.IntegerField(null=True, blank=True)
    HardWare_Ytilt6 = models.IntegerField(null=True, blank=True)
    HardWare_Ytilt7 = models.IntegerField(null=True, blank=True)
    HardWare_Ytilt8 = models.IntegerField(null=True, blank=True)
    HardWare_SN1 = models.CharField(max_length=20, blank=True)
    HardWare_SN2 = models.CharField(max_length=20, blank=True)
    HardWare_SN3 = models.CharField(max_length=20, blank=True)
    HardWare_SN4 = models.CharField(max_length=20, blank=True)
    HardWare_SN5 = models.CharField(max_length=20, blank=True)
    HardWare_SN6 = models.CharField(max_length=20, blank=True)
    HardWare_SN7 = models.CharField(max_length=20, blank=True)
    HardWare_SN8 = models.CharField(max_length=20, blank=True)
    HardWare_Adjust = models.CharField(max_length=20, blank=True)
    HardWare_PIP_X1 = models.IntegerField(null=True, blank=True, default=0)
    HardWare_PIP_X2 = models.IntegerField(null=True, blank=True, default=0)
    HardWare_PIP_X3 = models.IntegerField(null=True, blank=True, default=0)
    HardWare_PIP_X4 = models.IntegerField(null=True, blank=True, default=0)
    HardWare_PIP_X5 = models.IntegerField(null=True, blank=True, default=0)
    HardWare_PIP_X6 = models.IntegerField(null=True, blank=True, default=0)
    HardWare_PIP_X7 = models.IntegerField(null=True, blank=True, default=0)
    HardWare_PIP_X8 = models.IntegerField(null=True, blank=True, default=0)
    HardWare_PIP_Y1 = models.IntegerField(null=True, blank=True, default=0)
    HardWare_PIP_Y2 = models.IntegerField(null=True, blank=True, default=0)
    HardWare_PIP_Y3 = models.IntegerField(null=True, blank=True, default=0)
    HardWare_PIP_Y4 = models.IntegerField(null=True, blank=True, default=0)
    HardWare_PIP_Y5 = models.IntegerField(null=True, blank=True, default=0)
    HardWare_PIP_Y6 = models.IntegerField(null=True, blank=True, default=0)
    HardWare_PIP_Y7 = models.IntegerField(null=True, blank=True, default=0)
    HardWare_PIP_Y8 = models.IntegerField(null=True, blank=True, default=0)
    HardWare_PIP_Z1 = models.IntegerField(null=True, blank=True, default=0)
    HardWare_PIP_Z2 = models.IntegerField(null=True, blank=True, default=0)
    HardWare_PIP_Z3 = models.IntegerField(null=True, blank=True, default=0)
    HardWare_PIP_Z4 = models.IntegerField(null=True, blank=True, default=0)
    HardWare_PIP_Z5 = models.IntegerField(null=True, blank=True, default=0)
    HardWare_PIP_Z6 = models.IntegerField(null=True, blank=True, default=0)
    HardWare_PIP_Z7 = models.IntegerField(null=True, blank=True, default=0)
    HardWare_PIP_Z8 = models.IntegerField(null=True, blank=True, default=0)

    # 4.Perfomance
    Perfomance_CoverSafety = models.CharField(max_length=20, blank=True)
    Perfomance_Barcode = models.CharField(max_length=20, blank=True)
    Perfomance_XYZpositioning = models.CharField(max_length=20, blank=True)
    Perfomance_HHS_SN = models.CharField(max_length=20, blank=True)
    Perfomance_HHS_temperature = models.CharField(max_length=20, blank=True)
    Perfomance_HHS_RPM = models.CharField(max_length=20, blank=True)
    Perfomance_Loading_TipCarrier = models.CharField(max_length=20, blank=True)
    Perfomance_Loading_TubeCarrier = models.CharField(max_length=20, blank=True)
    Perfomance_Loading_mtpCarrier = models.CharField(max_length=20, blank=True)
    Perfomance_Loading_4mfxCarrier = models.CharField(max_length=20, blank=True)

    Perfomance_VFV_Accuracy300ul1 = models.CharField(max_length=20, blank=True)
    Perfomance_VFV_Accuracy300ul2 = models.CharField(max_length=20, blank=True)
    Perfomance_VFV_Accuracy300ul3 = models.CharField(max_length=20, blank=True)
    Perfomance_VFV_Accuracy300ul4 = models.CharField(max_length=20, blank=True)
    Perfomance_VFV_Accuracy300ul5 = models.CharField(max_length=20, blank=True)
    Perfomance_VFV_Accuracy300ul6 = models.CharField(max_length=20, blank=True)
    Perfomance_VFV_Accuracy300ul7 = models.CharField(max_length=20, blank=True)
    Perfomance_VFV_Accuracy300ul8 = models.CharField(max_length=20, blank=True)

    Perfomance_VFV_Precision300ul1 = models.CharField(max_length=20, blank=True)
    Perfomance_VFV_Precision300ul2 = models.CharField(max_length=20, blank=True)
    Perfomance_VFV_Precision300ul3 = models.CharField(max_length=20, blank=True)
    Perfomance_VFV_Precision300ul4 = models.CharField(max_length=20, blank=True)
    Perfomance_VFV_Precision300ul5 = models.CharField(max_length=20, blank=True)
    Perfomance_VFV_Precision300ul6 = models.CharField(max_length=20, blank=True)
    Perfomance_VFV_Precision300ul7 = models.CharField(max_length=20, blank=True)
    Perfomance_VFV_Precision300ul8 = models.CharField(max_length=20, blank=True)

    Perfomance_VFV_Accuracy1000ul1 = models.CharField(max_length=20, blank=True)
    Perfomance_VFV_Accuracy1000ul2 = models.CharField(max_length=20, blank=True)
    Perfomance_VFV_Accuracy1000ul3 = models.CharField(max_length=20, blank=True)
    Perfomance_VFV_Accuracy1000ul4 = models.CharField(max_length=20, blank=True)
    Perfomance_VFV_Accuracy1000ul5 = models.CharField(max_length=20, blank=True)
    Perfomance_VFV_Accuracy1000ul6 = models.CharField(max_length=20, blank=True)
    Perfomance_VFV_Accuracy1000ul7 = models.CharField(max_length=20, blank=True)
    Perfomance_VFV_Accuracy1000ul8 = models.CharField(max_length=20, blank=True)

    Perfomance_VFV_Precision1000ul1 = models.CharField(max_length=20, blank=True)
    Perfomance_VFV_Precision1000ul2 = models.CharField(max_length=20, blank=True)
    Perfomance_VFV_Precision1000ul3 = models.CharField(max_length=20, blank=True)
    Perfomance_VFV_Precision1000ul4 = models.CharField(max_length=20, blank=True)
    Perfomance_VFV_Precision1000ul5 = models.CharField(max_length=20, blank=True)
    Perfomance_VFV_Precision1000ul6 = models.CharField(max_length=20, blank=True)
    Perfomance_VFV_Precision1000ul7 = models.CharField(max_length=20, blank=True)
    Perfomance_VFV_Precision1000ul8 = models.CharField(max_length=20, blank=True)

    # 5.Attachment
    Attachment_CoverSafety_Report = models.CharField(max_length=20, null=True, blank=True)
    Attachment_Barcode_Report = models.CharField(max_length=20, null=True, blank=True)
    Attachment_Position_Report = models.CharField(max_length=20, null=True, blank=True)
    Attachment_Declaration_HHS = models.CharField(max_length=20, null=True, blank=True)
    Attachment_Declaration = models.CharField(max_length=20, null=True, blank=True)
    Attachment_Measurement_Protocol = models.CharField(max_length=20, null=True, blank=True)
    Attachment_ElectricalSafety_Report = models.CharField(max_length=20, null=True, blank=True)
    Attachment_CoverSafety_Report_File = models.FileField(upload_to=Attachment_image_path, null=True, blank=True)
    Attachment_Barcode_Report_File = models.FileField(upload_to=Attachment_image_path, null=True, blank=True)
    Attachment_Position_Report_File = models.FileField(upload_to=Attachment_image_path, null=True, blank=True)
    Attachment_Files = models.FileField(upload_to=test_path, null=True, blank=True)

    def __str__(self):
        return self.Instrument_SN_id


class Inspection_Category(models.Model):
    Category = models.CharField(max_length=30)
    Subcategory = models.CharField(max_length=60)

    def __str__(self):
        return self.Category
