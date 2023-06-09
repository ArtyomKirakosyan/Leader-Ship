# Generated by Django 4.2.1 on 2023-05-24 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_aboutphoto'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientMail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75, verbose_name='Title 1: ')),
                ('profesion', models.CharField(max_length=75, verbose_name='Profesion: ')),
                ('img', models.ImageField(upload_to='media', verbose_name='Img :')),
                ('facebook', models.URLField(verbose_name='Facebook: ')),
                ('instagram', models.URLField(verbose_name='Instagram :')),
                ('gmail', models.URLField(verbose_name='Gmail :')),
            ],
            options={
                'verbose_name': 'Client mail',
                'verbose_name_plural': 'Client mails',
            },
        ),
    ]
