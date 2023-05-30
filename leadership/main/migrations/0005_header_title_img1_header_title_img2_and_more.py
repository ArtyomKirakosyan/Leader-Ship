# Generated by Django 4.2.1 on 2023-05-24 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_header_img1_header_img2_header_img3'),
    ]

    operations = [
        migrations.AddField(
            model_name='header',
            name='title_img1',
            field=models.CharField(default=0, max_length=75, verbose_name='Img 1 title: '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='header',
            name='title_img2',
            field=models.CharField(default=0, max_length=75, verbose_name='Img 2 title: '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='header',
            name='title_img3',
            field=models.CharField(default=0, max_length=75, verbose_name='Img 3 title: '),
            preserve_default=False,
        ),
    ]