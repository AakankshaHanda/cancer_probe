# Generated by Django 3.0.5 on 2020-05-06 20:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_auto_20200506_1656'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctors',
            name='license_no',
        ),
        migrations.RemoveField(
            model_name='doctors',
            name='phone_num',
        ),
    ]
