# Generated by Django 4.0.3 on 2022-07-29 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Instrumentapp', '0012_alter_revision_instrument_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='revision',
            name='Type',
            field=models.CharField(choices=[('수입검사 성적서', '수입검사 성적서'), ('완제품검사 성적서', '완제품검사 성적서'), ('완제품 지침서', '완제품 지침서'), ('완제품 라벨', '완제품 라벨'), ('라벨링 포장 지침서', '라벨링 포장 지침서')], max_length=40, verbose_name='문서 구분'),
        ),
    ]