# Generated by Django 3.0.5 on 2020-05-12 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0021_remove_hospital_license_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='dateofopening',
            field=models.CharField(max_length=50),
        ),
    ]
