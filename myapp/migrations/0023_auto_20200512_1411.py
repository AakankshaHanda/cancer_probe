# Generated by Django 3.0.5 on 2020-05-12 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0022_auto_20200512_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='phone_num',
            field=models.CharField(max_length=50),
        ),
    ]
