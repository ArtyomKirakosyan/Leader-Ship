# Generated by Django 4.2.1 on 2023-05-25 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='header',
            name='date2',
            field=models.IntegerField(default=3, verbose_name='Untill: '),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='header',
            name='date',
            field=models.DateField(verbose_name='day'),
        ),
    ]
