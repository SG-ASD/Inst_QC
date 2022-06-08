from django.db import models

# Create your models here.
import os

from django.contrib.auth.models import User
from django.db import models
from Instrumentapp.models import Instrument
from django.urls import resolve
# Create your models here.
from django.http import request


class FinishInspection(models.Model):
    # 1:1 매칭 시켜준다. User 와 Profile 1:! 매칭
    # related_name = request.user.profile.nickname
    # user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    # def Attachment_image_path(instance, filename):
    #     # MEDEIA_ROOT/user_<pk>/ 경로로 <filename> 이름으로 업로드
    #     return f'{instance.Instrument_SN_id}/Attachment/{filename}'
    #
    # def Appearance_image_path(instance, filename):
    #     # MEDEIA_ROOT/user_<pk>/ 경로로 <filename> 이름으로 업로드
    #     return f'{instance.Instrument_SN_id}/Appearance/{filename}'

    # Inspection
    Name = models.CharField(max_length=60, blank=True)  # 장비명
    Instrument_SN = models.ForeignKey(Instrument, on_delete=models.CASCADE, db_column='Instrument_SN', related_name='Finished_Instrument_SN')  # 장비 SN
    Computer_SN = models.CharField(max_length=50, blank=True)  # 컴퓨터 SN
    Barcode_Scanner = models.CharField(max_length=50, blank=True)  # 바코드 스캐너
    Inspector = models.CharField(max_length=20, blank=True)  # 검사자
    Start_Date = models.DateField(null=True, blank=True)  # 검사시작일
    Completed_Date = models.DateField(null=True, blank=True)  # 검사완료일
    SW_Version = models.CharField(max_length=50, blank=True)  # SW 버전
    SL_Version = models.CharField(max_length=50, blank=True)  # 씨젠런처 버전
    Revision = models.CharField(max_length=50, blank=True)  # 검사성적서 Revision
    Status = models.CharField(max_length=20, blank=True)  # 검사 상태

    # 1. Computer verification
    Computer_Version = models.CharField(max_length=50, blank=True)  # 컴퓨터 OS 버전

    # 2. Seegene Launcher Installation process verification
    SL_Install = models.CharField(max_length=20, blank=True)  # 씨젠런처 정상설치 여부
    Method_Import = models.CharField(max_length=20, blank=True)  # 메소드 자동 Import 여부
    SL_Run_Version = models.CharField(max_length=20, blank=True)  # 씨젠런처 버전 및 정상구동 확인

    # 3. Communication test
    SL_Maintenance_Screen = models.CharField(max_length=20, blank=True)  # 씨젠런처 메인터넌스 화면 표시 및 적용 여부

    # 4. Seegene Launcher performance verification
    SL_Home_Screen = models.CharField(max_length=20, blank=True)  # 씨젠런처 홈 화면 표시 및 적용 여부
    SL_mode = models.CharField(max_length=20, blank=True)  # 씨젠런처 모드 전환 가능여부
    SL_Protocol = models.CharField(max_length=20, blank=True)  # 씨젠런처 프로토콜 생성 가능여부
    SL_Setting_Screen = models.CharField(max_length=20, blank=True)  # 씨젠런처 세팅 화면 전환 가능여부
    SL_Trace = models.CharField(max_length=20, blank=True)  # trace 파일 open 가능여부

    # 5. Labeling & Packaging inspection
    Condition = models.CharField(max_length=20, blank=True)  # Condition
    HHS_Labeled = models.CharField(max_length=20, blank=True)  # HHS_Labeled
    Acc_Labeled = models.CharField(max_length=20, blank=True)  # Acc_Labeled
    Labeling_Instruction_Rev = models.CharField(max_length=50, blank=True)  # Labeling_Instruction_Rev
    Labeling_Instruction = models.CharField(max_length=50, blank=True)  # Labeling_Instruction
    Labeling_Box = models.CharField(max_length=50, blank=True)  # Labeling_Instructio
    Label_SN = models.CharField(max_length=50, blank=True)  # Label_SN
    Label_MFG = models.CharField(max_length=20, blank=True)  # Label_MFG
    Label_Option = models.CharField(max_length=20, blank=True)  # 옵션 체크 가능여부
    UDI_Barcode = models.CharField(max_length=20, blank=True)  # 씨젠런처 바코드 구동 가능여부
    UDI_HRI = models.CharField(max_length=20, blank=True)  # 씨젠런처 바코드 구동 가능여부













