# Generated by Django 4.1.7 on 2024-06-12 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coursesapp', '0008_usercertificates'),
    ]

    operations = [
        migrations.CreateModel(
            name='userplacement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=25)),
                ('resume', models.FileField(upload_to='')),
            ],
        ),
    ]
