from django.db import models

# Create your models here.


class Instrument(models.Model):
    SN = models.CharField(primary_key=True, max_length=30, unique=True)  # 장비 SN
    Name = models.CharField(max_length=60)  # 장비명

    def __str__(self):
        return self.SN

class Revision(models.Model):
    Management_Num = models.CharField(max_length=50, verbose_name='관리번호')  # 관리번호
    Instrument_Name = models.CharField(
        # 튜플 안에 튜플
        choices=(
            # DB에 저장될 값과 사용자에게 보여줄 값
            ('Seegene STARlet', 'Seegene STARlet'),
            ('Hamilton STARlet', 'Hamilton STARlet'),
            ('Seegene Nimbus', 'Seegene Nimbus'),
            ('CFX 96Dx', 'CFX 96Dx'),
            ('SeePrep32', 'SeePrep32'),
            ('Labelling & Packaging Instruction', 'Labelling & Packaging Instruction'),
            ('Seegene STARlet-VCMS', 'Seegene STARlet-VCMS'),
            ('Seegene STARlet-UV Light Kit', 'Seegene STARlet-UV Light Kit'),
        ),
        default='Seegene STARlet', max_length=100, verbose_name='장비이름'
    )  # 장비명
    Type = models.CharField(
        choices=(
        # DB에 저장될 값과 사용자에게 보여줄 값
        ('수입검사 성적서', '수입검사 성적서'),
        ('완제품검사 성적서', '완제품검사 성적서'),
        ('완제품 지침서', '완제품 지침서'),
        ('완제품 라벨', '완제품 라벨'),
        ('라벨링 포장 지침서', '라벨링 포장 지침서'),
    ),
       max_length=40, verbose_name='문서 구분'
    )
    Revision = models.IntegerField(null=False)  # Revision
    Start_Dt = models.DateField(null=True, blank=True, verbose_name='사용 시작일')
    Expiry_Dt = models.DateField(null=True, blank=True, verbose_name='사용 종료일')
    UpperMNG_Num = models.CharField(null=True, blank=True, max_length=50, verbose_name='상위 관리번호')  # 관리번호
    Rev_UpperMNG_Rev = models.IntegerField(null=True, blank=True, verbose_name='상위 Reivision') # 지침서 Rev UpperMNG_Rev
    UpperRev_Date = models.DateField(null=True, blank=True, verbose_name='지침서 개정일')
    Remarks = models.CharField(max_length=300, verbose_name='비고', null=True, blank=True)

    class Meta:
        db_table = 'instrumentapp_revision'
        verbose_name = "개정문서 데이터"
        verbose_name_plural = "개정문서 데이터"

class Version(models.Model):
    Type = models.CharField(
        choices=(
        # DB에 저장될 값과 사용자에게 보여줄 값
        ('지침서용', '지침서용'),
        ('성적서용', '성적서용'),
    ),
       max_length=40, verbose_name='구분'
    )

    Instrument_Name = models.CharField(
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
        default='Seegene STARlet', max_length=32, verbose_name='장비명'
    )  # 장비명

    SW_Name = models.CharField(
        # 튜플 안에 튜플
        choices=(
            # DB에 저장될 값과 사용자에게 보여줄 값
            ('Microlab STAR Maintenance & Verification', 'Microlab STAR Maintenance & Verification'),
            ('STARlet Service-Shortcut Software', 'STARlet Service-Shortcut Software'),
            ('Hamilton STARlet', 'Hamilton STARlet'),
            ('VCMS Service Software', 'VCMS Service Software'),
            ('FourProbeCalibration', 'FourProbeCalibration'),
            ('Hamilton S/W Version', 'Hamilton S/W Version'),
            ('Hamilton FV2 Version', 'Hamilton FV2 Version'),
            ('Pipette Ch (PX)', 'Pipette Ch (PX)'),
            ('X-drive (XO)', 'X-drive (XO)'),
            ('Master (CO)', 'Master (CO)'),
            ('Inst_Label_Kor', '국문 장비 라벨'),
            ('Box_Label_Kor', '국문 박스 라벨'),
            ('Inst_Label_Eng', '영문 장비 라벨'),
            ('Box_Label_Eng', '영문 박스 라벨'),
            ('Hamilton S/W Version', 'Hamilton S/W Version'),
            ('Nimbus CO-RE', 'Nimbus CO-RE'),
            ('DAC0', 'DAC0'),
            ('Left/Right Door Lock', 'Left/Right Door Lock'),
            ('Barcode Scanner', 'Barcode Scanner'),
            ('Extraction System S/W Version', 'Extraction System S/W Version'),
            ('Firmware Version', 'Firmware Version'),
            ('Seegene Launcher Version', 'Seegene Launcher Version'),
        ),
        default='Seegene Launcher Version', max_length=100, verbose_name='소프트웨어명'
    )  # 장비명

    SW_Ver = models.CharField(max_length=200, null=True, blank=True, verbose_name='버전')
    # Pipette_Ch = models.CharField(max_length=50, null=True, blank=True, verbose_name='파이펫 채널 버전')
    # X_drive = models.CharField(max_length=50, null=True, blank=True, verbose_name='X-Drive 버전')
    # Master = models.CharField(max_length=50, null=True, blank=True, verbose_name='마스터 버전')
    # Launcher_Version = models.CharField(max_length=50, null=True, blank=True, verbose_name='런처 버전')
    # Nimbus_CORE = models.CharField(max_length=50, null=True, blank=True, verbose_name='님부스 CO-RE')
    # DAC0 = models.CharField(max_length=50, null=True, blank=True, verbose_name='님부스 DACO')
    # Door_Lock = models.CharField(max_length=50, null=True, blank=True, verbose_name='님부스 도어락')
    # Barcode_Scanner = models.CharField(max_length=50, null=True, blank=True, verbose_name='바코드 스캐너')
    # IO_Board = models.CharField(max_length=50, null=True, blank=True, verbose_name='IO 보드')
    # Extraction_System = models.CharField(max_length=50, null=True, blank=True, verbose_name='SeePrep32 Extraction System')
    # Firmware = models.CharField(max_length=50, null=True, blank=True, verbose_name='SeePrep32 Firmware')
    #
    #
    # Inst_Label_Kor = models.CharField(max_length=50, default='', blank=True, verbose_name='장비라벨(국문)') # 관리번호
    # Box_Label_Kor = models.CharField(max_length=50, default='', blank=True,  verbose_name='박스라벨(국문)') # Revision
    # Inst_Label_Eng = models.CharField(max_length=50, default='', blank=True,  verbose_name='박스라벨(영문)')
    # Box_Label_Eng = models.CharField(max_length=50, default='', blank=True,  verbose_name='박스라벨(영문)')




    Start_Dt = models.DateField(null=True, blank=True, verbose_name='사용 시작일')
    Expiry_Dt = models.DateField(null=True, blank=True, verbose_name='사용 종료일')
    Remarks = models.CharField(max_length=300, verbose_name='비고', null=True, blank=True)



    class Meta:
        db_table = 'instrumentapp_version'
        verbose_name = "장비 버전관리 데이터"
        verbose_name_plural = "장비 버전관리 데이터"