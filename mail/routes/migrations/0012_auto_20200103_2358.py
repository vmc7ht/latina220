# Generated by Django 2.2.6 on 2020-01-03 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0011_auto_20200103_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='route_ns',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Route NS (YYYY-MM-DD)'),
        ),
    ]
