# Generated by Django 3.0.5 on 2020-05-26 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0024_auto_20200513_1411'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='txtarea',
            new_name='message',
        ),
    ]
