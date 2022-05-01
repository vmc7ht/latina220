# Generated by Django 2.2.6 on 2020-01-06 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0014_auto_20200104_2222'),
    ]

    operations = [
        migrations.CreateModel(
            name='Override',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(blank=True, max_length=30, null=True, verbose_name='Date(YYYY-MM-DD)')),
                ('text', models.CharField(blank=True, max_length=10, null=True, verbose_name='text')),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='override', to='routes.Route')),
            ],
        ),
    ]
