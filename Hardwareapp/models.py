from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models

class Calibration(models.Model):
    Managemant_Num = models.CharField(primary_key=True, max_length=30, unique=True)  # 관리번호
    Instrument = models.CharField(max_length=60)  # 장비명
    Description = models.CharField(max_length=60)  # 설비 및 계측기
    State = models.CharField(max_length=60)  # 가능 
    Type = models.CharField(max_length=60)  # 유형
    Calibration_Date = models.DateField(auto_now=True) # 교정일자
    Validation_Date = models.DateField(auto_now=True) # 유효기간

    def __str__(self):
        return self.Calibration





