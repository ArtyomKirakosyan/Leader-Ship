# Generated by Django 4.2.1 on 2023-05-25 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_alter_schedulesinformation_people_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pricing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=75, verbose_name='Title: ')),
                ('price', models.IntegerField(verbose_name='Price: ')),
                ('offer', models.CharField(max_length=75, verbose_name='Offer: ')),
                ('place', models.CharField(max_length=75, verbose_name='Place : ')),
                ('support', models.CharField(max_length=75, verbose_name='Support time : ')),
                ('txt', models.TextField(verbose_name='Text :')),
            ],
            options={
                'verbose_name': 'Pricing',
                'verbose_name_plural': 'Pricings',
            },
        ),
        migrations.CreateModel(
            name='PricingTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=75, verbose_name='Title: ')),
            ],
            options={
                'verbose_name': 'Pricing title',
                'verbose_name_plural': 'Pricings title',
            },
        ),
        migrations.CreateModel(
            name='RegisterToday',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=75, verbose_name='Title: ')),
                ('txt', models.TextField(verbose_name='Text: ')),
            ],
            options={
                'verbose_name': 'RegisterToday',
                'verbose_name_plural': 'RegisterToday',
            },
        ),
    ]
