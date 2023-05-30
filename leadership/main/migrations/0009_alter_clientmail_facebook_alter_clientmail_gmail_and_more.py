# Generated by Django 4.2.1 on 2023-05-24 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_clientmail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientmail',
            name='facebook',
            field=models.URLField(blank=True, verbose_name='Facebook: '),
        ),
        migrations.AlterField(
            model_name='clientmail',
            name='gmail',
            field=models.URLField(blank=True, verbose_name='Gmail :'),
        ),
        migrations.AlterField(
            model_name='clientmail',
            name='instagram',
            field=models.URLField(blank=True, verbose_name='Instagram :'),
        ),
        migrations.AlterField(
            model_name='clientmail',
            name='name',
            field=models.CharField(max_length=75, verbose_name='Name: '),
        ),
    ]
