# Generated by Django 3.2.5 on 2022-07-27 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Settingsapp', '0011_auto_20220727_1006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='Inspection_Path',
            field=models.FilePathField(allow_files=False, allow_folders=True, path='\\\\10.10.102.76\\장비품질관리팀\\품질관리_장비inspection\\01 검사 성적서 관리', verbose_name='수입검사 파일 위치'),
        ),
    ]
