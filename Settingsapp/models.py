from django.db import models

# Create your models here.


class Settings(models.Model):
    upload_path = ""

    # 수입검사 관련 파일 업로드 위치
    Inspection_Path = models.FilePathField(
        path=r"\\10.10.102.76\장비품질관리팀\품질관리_장비inspection\01 검사 성적서 관리",
        allow_files=False,
        allow_folders=True,
        verbose_name='수입검사 파일 위치',
    )
    # 부적합검사 관련 파일 업로드 위치
    Nonconformance_Path = models.FilePathField(
        path=r"\\10.10.102.76\장비품질관리팀\품질관리_장비inspection\01 검사 성적서 관리",
        allow_files=False,
        allow_folders=True,
        verbose_name='부적합검사 파일 위치'
    )

    File_Upload = models.FileField(
        default=r"\\10.10.102.76\장비품질관리팀\품질관리_장비inspection\01 검사 성적서 관리",
        upload_to=r"\\10.10.102.76\장비품질관리팀\품질관리_장비inspection\01 검사 성적서 관리",
        max_length=100
    )

