# Generated by Django 4.2.1 on 2023-05-29 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0033_schedulesinformation_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedulesinformation',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='schedules', to='main.schedulesdays'),
        ),
    ]
