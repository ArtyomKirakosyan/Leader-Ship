# Generated by Django 4.2.1 on 2023-05-24 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=75, verbose_name='Header name: ')),
                ('date', models.DateField()),
                ('img', models.ImageField(upload_to='media', verbose_name='Header photo:')),
            ],
            options={
                'verbose_name': 'Header',
                'verbose_name_plural': 'Header',
            },
        ),
    ]
