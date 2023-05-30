# Generated by Django 4.2.1 on 2023-05-25 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_rename_aboutclient_speakerinformation_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SchedulesDays',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=70, verbose_name='Day: ')),
                ('date', models.DateField(verbose_name='Date: ')),
            ],
            options={
                'verbose_name': 'Schedule Day',
                'verbose_name_plural': 'Schedules Days',
            },
        ),
    ]
