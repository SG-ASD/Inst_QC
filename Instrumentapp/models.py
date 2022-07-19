from django.db import models

# Create your models here.


class Instrument(models.Model):
    SN = models.CharField(primary_key=True, max_length=30, unique=True)  # 장비 SN
    Name = models.CharField(max_length=60)  # 장비명

    def __str__(self):
        return self.SN

class Revision(models.Model):
    Instrument = models.CharField(
        # 튜플 안에 튜플
        choices=(
            # DB에 저장될 값과 사용자에게 보여줄 값
            ('공용', '공용'),
            ('Seegene STARlet', 'Seegene STARlet'),
            ('Hamilton STARlet', 'Hamilton STARlet'),
            ('Seegene Nimbus', 'Seegene Nimbus'),
            ('CFX 96Dx', 'CFX 96Dx'),
            ('Seeprep32', 'Seeprep32'),
            ('SGRT', 'SGRT'),
            ('AIOS', 'AIOS'),
            ('VCMS', 'VCMS'),
            ('모바일스테이션', '모바일스테이션'),
            ('기타', '기타'),
        ),
        default='Seegene STARlet', max_length=32, verbose_name='장비이름'
    )  # 장비명
    Report_Category = models.CharField(
        choices=(
        # DB에 저장될 값과 사용자에게 보여줄 값
        ('Inspection Report', '수입검사 성적서'),
        ('Finished Product Report', '완제품검사 성적서'),
        ('Finished Product Report Rev', '완제품 지침서'),
        ('Finished Label', '완제품 라벨'),
    ),
       max_length=40, verbose_name='성적서 종류'
    )
    Rev_Num = models.CharField(max_length=50, ) # 관리번호
    Rev = models.IntegerField(null=False) # Revision
    Start_Dt = models.DateField(auto_now=True, verbose_name='사용 시작일')
    End_Dt = models.DateField(auto_now=True, verbose_name='사용 종료일')

    class Meta:
        db_table = 'instrumentapp_revision'
        verbose_name = "개정문서 데이터"
        verbose_name_plural = "개정문서 데이터"