# Generated by Django 3.0.5 on 2020-05-05 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_report'),
    ]

    operations = [
        migrations.CreateModel(
            name='donation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doner_name', models.CharField(max_length=30)),
                ('amount', models.IntegerField(max_length=8)),
                ('dayofdonation', models.CharField(max_length=10)),
            ],
        ),
    ]
