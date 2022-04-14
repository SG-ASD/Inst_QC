from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Inspection(models.Model):
    # 1:1 매칭 시켜준다. User 와 Profile 1:! 매칭
    # related_name = request.user.profile.nickname
    # user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    Instrument_SN = models.CharField(max_length=50, null=False)  # 장비 SN
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

    def __str__(self):
        return self.Instrument_SN






