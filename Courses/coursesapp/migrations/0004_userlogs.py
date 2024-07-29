# Generated by Django 4.1.7 on 2024-06-09 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coursesapp', '0003_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='userlogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=25)),
                ('phone', models.CharField(max_length=25)),
                ('photo', models.FileField(upload_to='')),
                ('email', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=25)),
            ],
        ),
    ]
