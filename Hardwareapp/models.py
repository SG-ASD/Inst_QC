from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models

class Calibration(models.Model):
    Managemant_Num = models.CharField(primary_key=True, max_length=30, unique=True)  # 관리번호
    Calibration_Serial = models.CharField(max_length=60, blank=True)  # 시리얼번호
    Instrument = models.CharField(max_length=60)  # 장비명
    Description = models.CharField(max_length=60)  # 설비 및 계측기
    State = models.CharField(max_length=60)  # 상태
    Type = models.CharField(max_length=60)  # 교정 유형
    CalibrationCycle = models.CharField(max_length=20, blank=True) # 교정주기
    CalibrationDt = models.DateField(auto_now=True) # 교정일자
    ValidationDt = models.DateField(auto_now=True) # 유효기간
    Real_Calibration_Date = models.DateField(auto_now=True) # 유효기간
    Cal_Location = models.CharField(max_length=20, blank=True) # 교정처
    Manufacturer = models.CharField(max_length=20, blank=True) # 제조자
    Model_Serial = models.CharField(max_length=30, blank=True) # 모델번호
    ERP_Nm = models.CharField(max_length=20, blank=True) # ERP 명칭
    ERP_Num = models.CharField(max_length=20, blank=True) # ERP 번호
    ERP_Sticker = models.CharField(max_length=20, blank=True) # ERP 라벨 부착여부
    ERP_Date = models.DateField(auto_now=True) # ERP 취득일자
    Main_Manager = models.CharField(max_length=20, blank=True) # 관리책임자(정)
    Sub_Manager = models.CharField(max_length=20, blank=True) # 관리책임자(부)
    Store_Location = models.CharField(max_length=20, blank=True) # 보관위치
    Previous_Manage_Num = models.CharField(max_length=40, blank=True) # 구 관리번호
    Etc = models.CharField(max_length=50, blank=True) # 비고
    Hide = models.IntegerField(null=True, blank=True) # 숨김여부



    def __str__(self):
        return self.Calibration





