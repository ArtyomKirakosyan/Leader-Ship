# Generated by Django 4.2.1 on 2023-05-25 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_schedulesinformation_place'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedulesinformation',
            name='name',
            field=models.CharField(max_length=75, null=True, verbose_name='Name: '),
        ),
        migrations.AlterField(
            model_name='schedulesinformation',
            name='people_img',
            field=models.ImageField(null=True, upload_to='media', verbose_name='People img :'),
        ),
        migrations.AlterField(
            model_name='schedulesinformation',
            name='profesion',
            field=models.CharField(max_length=75, null=True, verbose_name='Profesion: '),
        ),
    ]
