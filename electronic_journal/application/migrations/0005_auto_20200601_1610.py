# Generated by Django 3.0.6 on 2020-06-01 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0004_auto_20200601_1303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='daily_timetable',
            name='lessons',
        ),
        migrations.AddField(
            model_name='daily_timetable',
            name='lessons',
            field=models.CharField(default=1, help_text='выберете уроки', max_length=30),
            preserve_default=False,
        ),
    ]
