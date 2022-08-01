from django.db import models

# Create your models here.


# 부적합 검사 테이블
class Nonconformance(models.Model):
    # Summary
    ID = models.AutoField(primary_key=True)  # 고유값 PK
    Instrument_SN = models.CharField(max_length=200, blank=True)  # 장비 SN
    Computer_SN = models.CharField(max_length=200, blank=True)  # 컴퓨터 SN
    Name = models.CharField(max_length=200, blank=True)  # 장비명
    Inspector = models.CharField(max_length=200, blank=True)  # 검사자
    Start_Date = models.DateField(null=True, blank=True)  # 검사시작일
    Doc_Num = models.CharField(max_length=200, blank=True)  # 성적서 Revision
    Revision = models.IntegerField(blank=True, null=True)  # 문서버전
    Issue_Num = models.CharField(max_length=200, blank=True)  # 문서 발행 번호
    Category = models.CharField(max_length=200, blank=True)  # 부적합 발생 항목
    Attachment = models.TextField(blank=True)  # 첨부파일

    # Electrical Test
    Power_SWFunction = models.TextField(blank=True)
    Power_SWFunction_Detail = models.TextField(blank=True)
    Power_LED = models.TextField(blank=True)
    Power_LED_Detail = models.TextField(blank=True)

    # Hardware Adjustment
    ArmZ_Code = models.TextField(blank=True)
    ArmZ_Repetition = models.IntegerField(blank=True, null=True)
    ArmZ_Value_L = models.FloatField(blank=True, null=True)
    ArmZ_Value_R = models.FloatField(blank=True, null=True)
    ArmZ_State = models.TextField(blank=True)
    ArmDiff_Code = models.TextField(blank=True)
    ArmDiff_Repetition = models.IntegerField(blank=True, null=True)
    ArmDiff_Value = models.FloatField(blank=True, null=True)
    ArmDiff_State = models.TextField(blank=True)

    AdjustPIP_P1_Code = models.TextField(blank=True)
    AdjustPIP_P1_Repetition = models.IntegerField(blank=True, null=True)
    AdjustPIP_P1_Xdev = models.FloatField(blank=True, null=True)
    AdjustPIP_P1_Xtilt = models.FloatField(blank=True, null=True)
    AdjustPIP_P1_Ytilt = models.FloatField(blank=True, null=True)
    AdjustPIP_P1_State = models.TextField(blank=True)
    AdjustPIP_P2_Code = models.TextField(blank=True)
    AdjustPIP_P2_Repetition = models.IntegerField(blank=True, null=True)
    AdjustPIP_P2_Xdev = models.FloatField(blank=True, null=True)
    AdjustPIP_P2_Xtilt = models.FloatField(blank=True, null=True)
    AdjustPIP_P2_Ytilt = models.FloatField(blank=True, null=True)
    AdjustPIP_P2_State = models.TextField(blank=True)
    AdjustPIP_P3_Code = models.TextField(blank=True)
    AdjustPIP_P3_Repetition = models.IntegerField(blank=True, null=True)
    AdjustPIP_P3_Xdev = models.FloatField(blank=True, null=True)
    AdjustPIP_P3_Xtilt = models.FloatField(blank=True, null=True)
    AdjustPIP_P3_Ytilt = models.FloatField(blank=True, null=True)
    AdjustPIP_P3_State = models.TextField(blank=True)
    AdjustPIP_P4_Code = models.TextField(blank=True)
    AdjustPIP_P4_Repetition = models.IntegerField(blank=True, null=True)
    AdjustPIP_P4_Xdev = models.FloatField(blank=True, null=True)
    AdjustPIP_P4_Xtilt = models.FloatField(blank=True, null=True)
    AdjustPIP_P4_Ytilt = models.FloatField(blank=True, null=True)
    AdjustPIP_P4_State = models.TextField(blank=True)
    AdjustPIP_P5_Code = models.TextField(blank=True)
    AdjustPIP_P5_Repetition = models.IntegerField(blank=True, null=True)
    AdjustPIP_P5_Xdev = models.FloatField(blank=True, null=True)
    AdjustPIP_P5_Xtilt = models.FloatField(blank=True, null=True)
    AdjustPIP_P5_Ytilt = models.FloatField(blank=True, null=True)
    AdjustPIP_P5_State = models.TextField(blank=True)
    AdjustPIP_P6_Code = models.TextField(blank=True)
    AdjustPIP_P6_Repetition = models.IntegerField(blank=True, null=True)
    AdjustPIP_P6_Xdev = models.FloatField(blank=True, null=True)
    AdjustPIP_P6_Xtilt = models.FloatField(blank=True, null=True)
    AdjustPIP_P6_Ytilt = models.FloatField(blank=True, null=True)
    AdjustPIP_P6_State = models.TextField(blank=True)
    AdjustPIP_P7_Code = models.TextField(blank=True)
    AdjustPIP_P7_Repetition = models.IntegerField(blank=True, null=True)
    AdjustPIP_P7_Xdev = models.FloatField(blank=True, null=True)
    AdjustPIP_P7_Xtilt = models.FloatField(blank=True, null=True)
    AdjustPIP_P7_Ytilt = models.FloatField(blank=True, null=True)
    AdjustPIP_P7_State = models.TextField(blank=True)
    AdjustPIP_P8_Code = models.TextField(blank=True)
    AdjustPIP_P8_Repetition = models.IntegerField(blank=True, null=True)
    AdjustPIP_P8_Xdev = models.FloatField(blank=True, null=True)
    AdjustPIP_P8_Xtilt = models.FloatField(blank=True, null=True)
    AdjustPIP_P8_Ytilt = models.FloatField(blank=True, null=True)
    AdjustPIP_P8_State = models.TextField(blank=True)
    AdjustPIP_Code = models.TextField(blank=True)
    AdjustPIP_Repetition = models.IntegerField(blank=True, null=True)
    AdjustPIP_Fail = models.CharField(max_length=20, blank=True)
    CheckPIP_P1_Code = models.TextField(blank=True)
    CheckPIP_P1_Repetition = models.IntegerField(blank=True, null=True)
    CheckPIP_P1_X = models.FloatField(blank=True, null=True)
    CheckPIP_P1_Y = models.FloatField(blank=True, null=True)
    CheckPIP_P1_Z = models.FloatField(blank=True, null=True)
    CheckPIP_P1_State = models.TextField(blank=True)
    CheckPIP_P2_Code = models.TextField(blank=True)
    CheckPIP_P2_Repetition = models.IntegerField(blank=True, null=True)
    CheckPIP_P2_X = models.FloatField(blank=True, null=True)
    CheckPIP_P2_Y = models.FloatField(blank=True, null=True)
    CheckPIP_P2_Z = models.FloatField(blank=True, null=True)
    CheckPIP_P2_State = models.TextField(blank=True)
    CheckPIP_P3_Code = models.TextField(blank=True)
    CheckPIP_P3_Repetition = models.IntegerField(blank=True, null=True)
    CheckPIP_P3_X = models.FloatField(blank=True, null=True)
    CheckPIP_P3_Y = models.FloatField(blank=True, null=True)
    CheckPIP_P3_Z = models.FloatField(blank=True, null=True)
    CheckPIP_P3_State = models.TextField(blank=True)
    CheckPIP_P4_Code = models.TextField(blank=True)
    CheckPIP_P4_Repetition = models.IntegerField(blank=True, null=True)
    CheckPIP_P4_X = models.FloatField(blank=True, null=True)
    CheckPIP_P4_Y = models.FloatField(blank=True, null=True)
    CheckPIP_P4_Z = models.FloatField(blank=True, null=True)
    CheckPIP_P4_State = models.TextField(blank=True)
    CheckPIP_P5_Code = models.TextField(blank=True)
    CheckPIP_P5_Repetition = models.IntegerField(blank=True, null=True)
    CheckPIP_P5_X = models.FloatField(blank=True, null=True)
    CheckPIP_P5_Y = models.FloatField(blank=True, null=True)
    CheckPIP_P5_Z = models.FloatField(blank=True, null=True)
    CheckPIP_P5_State = models.TextField(blank=True)
    CheckPIP_P6_Code = models.TextField(blank=True)
    CheckPIP_P6_Repetition = models.IntegerField(blank=True, null=True)
    CheckPIP_P6_X = models.FloatField(blank=True, null=True)
    CheckPIP_P6_Y = models.FloatField(blank=True, null=True)
    CheckPIP_P6_Z = models.FloatField(blank=True, null=True)
    CheckPIP_P6_State = models.TextField(blank=True)
    CheckPIP_P7_Code = models.TextField(blank=True)
    CheckPIP_P7_Repetition = models.IntegerField(blank=True, null=True)
    CheckPIP_P7_X = models.FloatField(blank=True, null=True)
    CheckPIP_P7_Y = models.FloatField(blank=True, null=True)
    CheckPIP_P7_Z = models.FloatField(blank=True, null=True)
    CheckPIP_P7_State = models.TextField(blank=True)
    CheckPIP_P8_Code = models.TextField(blank=True)
    CheckPIP_P8_Repetition = models.IntegerField(blank=True, null=True)
    CheckPIP_P8_X = models.FloatField(blank=True, null=True)
    CheckPIP_P8_Y = models.FloatField(blank=True, null=True)
    CheckPIP_P8_Z = models.FloatField(blank=True, null=True)
    CheckPIP_P8_State = models.TextField(blank=True)

    # Performance Verification
    Cover_Safety_Front_State = models.TextField(blank=True)
    Cover_Safety_Right_State = models.TextField(blank=True)
    Cover_Safety_Detail = models.TextField(blank=True)
    Barcode_Horizontal = models.CharField(max_length=200, blank=True)
    Barcode_Vertical = models.CharField(max_length=200, blank=True)
    Barcode_Detail = models.TextField(blank=True)
    XYZ_Position_Code = models.TextField(blank=True)
    XYZ_Position_State = models.TextField(blank=True)
    XYZ_Position_Detail = models.TextField(blank=True)
    HHS_temperature = models.TextField(blank=True)
    HHS_RPM = models.TextField(blank=True)
    HHS_Detail = models.TextField(blank=True)
    Tip_Carrier = models.TextField(blank=True)
    Tube_Carrier = models.TextField(blank=True)
    MTP_Carrier = models.TextField(blank=True)
    MFX_Carrier = models.TextField(blank=True)
    Carrier_Detail = models.TextField(blank=True)

    VFV_P1_300ul = models.TextField(blank=True)
    VFV_P1_1000ul = models.TextField(blank=True)
    VFV_P2_300ul = models.TextField(blank=True)
    VFV_P2_1000ul = models.TextField(blank=True)
    VFV_P3_300ul = models.TextField(blank=True)
    VFV_P3_1000ul = models.TextField(blank=True)
    VFV_P4_300ul = models.TextField(blank=True)
    VFV_P4_1000ul = models.TextField(blank=True)
    VFV_P5_300ul = models.TextField(blank=True)
    VFV_P5_1000ul = models.TextField(blank=True)
    VFV_P6_300ul = models.TextField(blank=True)
    VFV_P6_1000ul = models.TextField(blank=True)
    VFV_P7_300ul = models.TextField(blank=True)
    VFV_P7_1000ul = models.TextField(blank=True)
    VFV_P8_300ul = models.TextField(blank=True)
    VFV_P8_1000ul = models.TextField(blank=True)
    VFV_Detail = models.TextField(blank=True)

    # Others
    Others = models.TextField(blank=True)

    def __str__(self):
        return f"{self.Name}_{self.Instrument_SN}"


# 부적합 검사 추가 항목 테이블
class Add_Nonconformance(models.Model):
    ID = models.ForeignKey(Nonconformance, on_delete=models.CASCADE, related_name='Add')  # 장비 SN
    Category = models.CharField(max_length=200, blank=True)  # 부적합 발생 항목
    Type = models.CharField(max_length=200, blank=True)  # 부적합 세부항목
    Part_Num = models.CharField(max_length=200, blank=True)  # 파트 번호
    Part_Name = models.TextField(blank=True)  # 파트 이름
    Part_Check = models.TextField(blank=True)  # 상태 체크
    Part_Detail = models.TextField(blank=True)  # 사진, 설명
    Part_Location = models.CharField(max_length=200, blank=True)  # 위치
    Part_Qty = models.IntegerField(blank=True, null=True)  # 파트 개수


# 부적합 항목 참조 테이블
class Ref_Nonconformance(models.Model):
    Category = models.CharField(max_length=200, blank=True)  # 부적합 발생 항목
    Type = models.CharField(max_length=200, blank=True)  # 부적합 세부항목
    Part_Num = models.CharField(max_length=200, blank=True, null=True)  # 파트 번호
    Part_Name = models.TextField(blank=True, null=True)  # 파트 이름
