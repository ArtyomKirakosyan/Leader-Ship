# Generated by Django 4.2.1 on 2023-05-25 16:08

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_alter_schedulesinformation_people_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=75, verbose_name='Header: ')),
                ('title', models.CharField(max_length=75, verbose_name='Title: ')),
                ('adress', models.CharField(max_length=255, verbose_name='Adress: ')),
                ('emai', models.EmailField(max_length=254, verbose_name='Email: ')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Phone: ')),
            ],
            options={
                'verbose_name': 'Venue',
                'verbose_name_plural': 'Venues',
            },
        ),
    ]
