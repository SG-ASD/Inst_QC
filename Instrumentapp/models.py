from django.db import models

# Create your models here.


class Instrument(models.Model):
    SN = models.CharField(max_length=30, unique=True)  # 장비 SN
    Name = models.CharField(max_length=60)  # 장비명

    def __str__(self):
        return self.SN


class Inspection(models.Model):
    SN = models.CharField(max_length=30, unique=True)  # 장비 SN
    Name = models.CharField(max_length=60)  # 장비명
    Computer_SN = models.CharField(max_length=30, blank=True)  # 컴퓨터 SN
    Start_Date = models.CharField(max_length=30, blank=True)  # 검사시작일
    Completed_Date = models.CharField(max_length=30, blank=True)  # 검사완료일
    Inspector = models.CharField(max_length=30, blank=True)  # 검사자
    Status = models.CharField(max_length=30, blank=True)  # 검사 상태
    Revision = models.CharField(max_length=40, blank=True)  # 검사성적서 Revision
    SW_Version = models.CharField(max_length=30, blank=True)  # SW 버전
    FV2_Version = models.CharField(max_length=30, blank=True)  # FV2 버전
    FW_PipetteCh = models.CharField(max_length=40, blank=True)  # PipetteCh 버전
    FW_Xdrive = models.CharField(max_length=40, blank=True)  # X-drive 버전
    FW_Master = models.CharField(max_length=40, blank=True)  # Master 버전

    def __str__(self):
        return self.SN
