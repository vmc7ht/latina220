# Generated by Django 2.2.6 on 2020-01-08 01:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0023_auto_20200107_1828'),
    ]

    operations = [
        migrations.CreateModel(
            name='Override_T6',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Date(YYYY-MM-DD)')),
                ('text', models.CharField(blank=True, max_length=10, null=True, verbose_name='text')),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='overrideT6', to='routes.Route')),
            ],
        ),
    ]
