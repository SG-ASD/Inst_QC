# Generated by Django 4.0.3 on 2022-07-26 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Instrumentapp', '0006_version_type_alter_version_sw_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='version',
            name='Etc',
        ),
        migrations.AddField(
            model_name='version',
            name='Remarks',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='비고'),
        ),
        migrations.AddField(
            model_name='version',
            name='SW_Ver',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='버전'),
        ),
        migrations.AlterField(
            model_name='version',
            name='Instrument_Name',
            field=models.CharField(choices=[('공용', '공용'), ('Seegene STARlet', 'Seegene STARlet'), ('Hamilton STARlet', 'Hamilton STARlet'), ('Seegene Nimbus', 'Seegene Nimbus'), ('CFX 96Dx', 'CFX 96Dx'), ('Seeprep32', 'Seeprep32'), ('SGRT', 'SGRT'), ('AIOS', 'AIOS'), ('VCMS', 'VCMS'), ('모바일스테이션', '모바일스테이션'), ('기타', '기타')], default='Seegene STARlet', max_length=32, verbose_name='장비명'),
        ),
        migrations.AlterField(
            model_name='version',
            name='SW_Name',
            field=models.CharField(choices=[('Microlab STAR Maintenance & Verification', 'Microlab STAR Maintenance & Verification'), ('STARlet Service-Shortcut Software', 'STARlet Service-Shortcut Software'), ('Hamilton STARlet', 'Hamilton STARlet'), ('VCMS Service Software', 'VCMS Service Software'), ('FourProbeCalibration', 'FourProbeCalibration'), ('Hamilton S/W Version', 'Hamilton S/W Version'), ('Hamilton FV2 Version', 'Hamilton FV2 Version'), ('Pipette Ch (PX)', 'Pipette Ch (PX)'), ('X-drive (XO)', 'X-drive (XO)'), ('Master (CO)', 'Master (CO)'), ('Inst_Label_Kor', '국문 장비 라벨'), ('Box_Label_Kor', '국문 박스 라벨'), ('Inst_Label_Eng', '영문 장비 라벨'), ('Box_Label_Eng', '영문 박스 라벨'), ('Hamilton S/W Version', 'Hamilton S/W Version'), ('Nimbus CO-RE', 'Nimbus CO-RE'), ('DAC0', 'DAC0'), ('Left/Right Door Lock', 'Left/Right Door Lock'), ('Barcode Scanner', 'Barcode Scanner'), ('Extraction System S/W Version', 'Extraction System S/W Version'), ('Firmware Version', 'Firmware Version'), ('Seegene Launcher Version', 'Seegene Launcher Version')], default='Seegene Launcher Version', max_length=100, verbose_name='소프트웨어명'),
        ),
        migrations.AlterField(
            model_name='version',
            name='Type',
            field=models.CharField(choices=[('지침서용', '지침서용'), ('성적서용', '성적서용')], max_length=40, verbose_name='구분'),
        ),
    ]
