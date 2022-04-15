# Generated by Django 4.0.3 on 2022-04-15 06:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Instrumentapp', '0011_remove_instrument_id_alter_instrument_sn'),
        ('Inspectionapp', '0012_alter_inspection_instrument_sn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inspection',
            name='Instrument_SN',
            field=models.ForeignKey(db_column='Instrument_SN', on_delete=django.db.models.deletion.CASCADE, to='Instrumentapp.instrument'),
        ),
    ]
