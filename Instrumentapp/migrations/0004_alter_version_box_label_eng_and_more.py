# Generated by Django 4.0.3 on 2022-07-25 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Instrumentapp', '0003_rename_instrument_version_instrument_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='version',
            name='Box_Label_Eng',
            field=models.CharField(blank=True, default='', max_length=50, verbose_name='박스라벨(영문)'),
        ),
        migrations.AlterField(
            model_name='version',
            name='Box_Label_Kor',
            field=models.CharField(blank=True, default='', max_length=50, verbose_name='박스라벨(국문)'),
        ),
        migrations.AlterField(
            model_name='version',
            name='Inst_Label_Eng',
            field=models.CharField(blank=True, default='', max_length=50, verbose_name='박스라벨(영문)'),
        ),
        migrations.AlterField(
            model_name='version',
            name='Inst_Label_Kor',
            field=models.CharField(blank=True, default='', max_length=50, verbose_name='장비라벨(국문)'),
        ),
    ]
