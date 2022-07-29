from django.db import models

# Create your models here.


class Settings(models.Model):
    upload_path = ""
    Type = models.CharField(
        choices=(
            # DB에 저장될 값과 사용자에게 보여줄 값
            ('수입검사', '수입검사'),
            ('완제품검사', '완제품검사'),
        ),
        max_length=40, verbose_name='구분'
    )
    Path = models.CharField(max_length=300, blank=True, null=True, verbose_name='폴더경로')  # 폴더 경로
    Path_Describe = models.CharField(max_length=60, blank=True, null=True, verbose_name='설명')  # 폴더 설명

    # # 수입검사 관련 파일 업로드 위치
    # Inspection_Path = models.FilePathField(
    #     path=r"\\10.10.102.76\장비품질관리팀\품질관리_장비inspection\01 검사 성적서 관리",
    #     allow_files=False,
    #     allow_folders=True,
    #     verbose_name='수입검사 파일 위치',
    # )
    # 부적합검사 관련 파일 업로드 위치
    # Nonconformance_Path = models.FilePathField(
    #     path=r"\\10.10.102.76\장비품질관리팀\품질관리_장비inspection\01 검사 성적서 관리",
    #     allow_files=False,
    #     allow_folders=True,
    #     verbose_name='부적합검사 파일 위치'
    # )
    # 
    # File_Upload = models.FileField(
    #     default=r"\\10.10.102.76\장비품질관리팀\품질관리_장비inspection\01 검사 성적서 관리",
    #     upload_to=r"\\10.10.102.76\장비품질관리팀\품질관리_장비inspection\01 검사 성적서 관리",
    #     max_length=100
    # )

