# Generated by Django 2.2.6 on 2020-01-07 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0019_delete_t6_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='route',
            name='T6_type',
            field=models.CharField(max_length=30, null=True, verbose_name='T6 Type'),
        ),
    ]
