# Generated by Django 4.2.1 on 2023-05-25 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_alter_schedulesinformation_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedulesinformation',
            name='name',
            field=models.CharField(blank=True, default=1, max_length=75, verbose_name='Name: '),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='schedulesinformation',
            name='profesion',
            field=models.CharField(blank=True, default=1, max_length=75, verbose_name='Profesion: '),
            preserve_default=False,
        ),
    ]
