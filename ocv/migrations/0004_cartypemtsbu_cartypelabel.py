# Generated by Django 2.1 on 2018-09-21 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ocv', '0003_auto_20180921_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartypemtsbu',
            name='carTypeLabel',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ocv.CarTypeLabel'),
            preserve_default=False,
        ),
    ]
