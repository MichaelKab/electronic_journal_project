# Generated by Django 3.0.6 on 2020-06-03 10:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0005_auto_20200601_1610'),
    ]

    operations = [
        migrations.AddField(
            model_name='classes',
            name='students',
            field=models.ManyToManyField(help_text='выберите учеников', to='application.Users'),
        ),
        migrations.AlterField(
            model_name='classes',
            name='grade',
            field=models.CharField(help_text='класс', max_length=4),
        ),
        migrations.AlterField(
            model_name='daily_timetable',
            name='Day',
            field=models.CharField(choices=[('Пн', 'Понедельник'), ('Вт', 'Вторник'), ('Ср', 'Среда'), ('Чт', 'Четверг'), ('Пт', 'Пятница'), ('Сб', 'Суббота'), ('Вс', 'Воскресенье')], default=datetime.date(2020, 6, 3), help_text='выберете день', max_length=11),
        ),
        migrations.AlterField(
            model_name='home_work',
            name='text',
            field=models.CharField(help_text='текст ДЗ', max_length=100),
        ),
        migrations.CreateModel(
            name='score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.CharField(help_text='оценка', max_length=3)),
                ('school_subject', models.ManyToManyField(help_text='урок', to='application.lesson')),
                ('teacher', models.ManyToManyField(help_text='учитель', to='application.Users')),
            ],
        ),
    ]
