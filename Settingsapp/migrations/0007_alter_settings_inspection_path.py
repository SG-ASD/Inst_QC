# Generated by Django 3.2.5 on 2022-07-26 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Settingsapp', '0006_auto_20220726_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='Inspection_Path',
            field=models.FilePathField(allow_files=False, allow_folders=True, path='\\\\10.10.102.76\\추출장비다원화팀\\테스트', verbose_name='수입검사 파일 위치'),
        ),
    ]