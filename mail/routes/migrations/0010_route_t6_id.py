# Generated by Django 2.2.6 on 2020-01-02 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0009_auto_20200102_0244'),
    ]

    operations = [
        migrations.AddField(
            model_name='route',
            name='T6_id',
            field=models.CharField(max_length=30, null=True, verbose_name='Route NS'),
        ),
    ]
