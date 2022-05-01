# Generated by Django 2.2.6 on 2020-01-03 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0010_route_t6_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='route',
            name='route_carrier_type',
        ),
        migrations.AlterField(
            model_name='route',
            name='route_zone',
            field=models.CharField(choices=[('20110', '20110'), ('20109', '20109')], default=None, max_length=30, null=True, verbose_name='Route Zone'),
        ),
    ]
