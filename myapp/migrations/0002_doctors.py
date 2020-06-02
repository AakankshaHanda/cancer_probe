# Generated by Django 3.0.5 on 2020-05-05 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='doctors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Qual', models.CharField(max_length=30)),
                ('license_no', models.IntegerField()),
                ('nationality', models.CharField(max_length=20)),
                ('phone_num', models.CharField(max_length=10)),
                ('Speciality', models.CharField(max_length=30)),
                ('experience', models.IntegerField()),
                ('address', models.TextField(max_length=50)),
                ('City', models.CharField(max_length=10)),
                ('photo', models.ImageField(blank=True, upload_to='data')),
            ],
        ),
    ]
