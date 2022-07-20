# Generated by Django 4.0.3 on 2022-07-19 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calibration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Instrument', models.CharField(choices=[('공용', '공용'), ('Seegene STARlet', 'Seegene STARlet'), ('Hamilton STARlet', 'Hamilton STARlet'), ('Seegene Nimbus', 'Seegene Nimbus'), ('CFX 96Dx', 'CFX 96Dx'), ('Seeprep32', 'Seeprep32'), ('SGRT', 'SGRT'), ('AIOS', 'AIOS'), ('VCMS', 'VCMS'), ('모바일스테이션', '모바일스테이션'), ('기타', '기타')], default='Seegene STARlet', max_length=32, verbose_name='장비')),
                ('Mgt_Num', models.CharField(max_length=30, unique=True, verbose_name='관리번호')),
                ('Equipment_Name', models.CharField(max_length=60, null=True, verbose_name='설비 및 계측기')),
                ('Status', models.CharField(choices=[('가능', '가능'), ('교정예정', '교정예정'), ('교정중', '교정중'), ('불가(고장)', '불가(고장)'), ('불가(기타)', '불가(기타)'), ('불가(미등록)', '불가(미등록)'), ('불가(미입고)', '불가(미입고)')], default='가능', max_length=32, verbose_name='상태')),
                ('CAL_Type', models.CharField(max_length=60, null=True, verbose_name='교정유형')),
                ('CAL_Cycle', models.CharField(blank=True, max_length=20, null=True, verbose_name='교정주기')),
                ('CAL_Date', models.DateField(blank=True, null=True, verbose_name='교정일자')),
                ('Expiration_Date', models.DateField(blank=True, null=True, verbose_name='유효기간')),
                ('Expiration_YYMM', models.DateField(auto_now=True, verbose_name='유효년월')),
                ('CAL_Plan_Date', models.DateField(auto_now=True, verbose_name='교정계획일자')),
                ('CAL_Company', models.CharField(blank=True, max_length=20, null=True, verbose_name='교정처')),
                ('CAL_Plan_Company', models.CharField(blank=True, max_length=20, null=True, verbose_name='교정예정처')),
                ('CAL_Plan_Price', models.IntegerField(blank=True, null=True, verbose_name='교정 예정금액')),
                ('CAL_Plan_Check', models.CharField(blank=True, max_length=20, null=True, verbose_name='교정계획확인')),
                ('MFG_Company', models.CharField(blank=True, max_length=20, null=True, verbose_name='제조사')),
                ('Model_Num', models.CharField(blank=True, max_length=30, null=True, verbose_name='모델번호')),
                ('Serial_Num', models.CharField(blank=True, max_length=60, verbose_name='시리얼번호')),
                ('ERP_Name', models.CharField(blank=True, max_length=20, null=True, verbose_name='ERP명칭')),
                ('ERP_Num', models.CharField(blank=True, max_length=20, null=True, verbose_name='ERP등록번호')),
                ('ERP_Label_State', models.CharField(blank=True, max_length=20, null=True, verbose_name='ERP 라벨부착여부')),
                ('ERP_Date', models.DateField(auto_now=True, null=True, verbose_name='ERP 취득일자')),
                ('Head', models.CharField(blank=True, max_length=20, null=True, verbose_name='관리책임자(정)')),
                ('Deputy_Head', models.CharField(blank=True, max_length=20, null=True, verbose_name='관리책임자(부)')),
                ('Store_Location', models.CharField(blank=True, max_length=20, null=True, verbose_name='보관위치')),
                ('Prev_Mgt_Num', models.CharField(blank=True, max_length=40, null=True, verbose_name='구 관리번호')),
                ('Price', models.IntegerField(blank=True, null=True, verbose_name='구매가격')),
                ('Ramarks', models.CharField(blank=True, max_length=50, null=True, verbose_name='비고')),
                ('is_Hide', models.BooleanField(default=True, null=True, verbose_name='공개여부')),
            ],
            options={
                'verbose_name': '교정Tool 데이터',
                'verbose_name_plural': '교정Tool 데이터',
                'db_table': 'Hardwareapp_calibration',
            },
        ),
    ]
