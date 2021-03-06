# Generated by Django 3.0.6 on 2020-06-01 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_auto_20200601_1238'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('middle_name', models.CharField(max_length=200)),
                ('status', models.CharField(blank=True, choices=[('s', 'student'), ('t', 'teacher')], default='student', max_length=7)),
            ],
        ),
        migrations.RemoveField(
            model_name='classes',
            name='the_letter_class',
        ),
        migrations.AlterField(
            model_name='classes',
            name='grade',
            field=models.CharField(help_text='выберете класс', max_length=1),
        ),
        migrations.CreateModel(
            name='Home_work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_start', models.DateTimeField(blank=True, null=True)),
                ('deadline', models.DateTimeField(blank=True, null=True)),
                ('text', models.CharField(help_text='текст ДЗ', max_length=1)),
                ('materials', models.FileField(upload_to=None)),
                ('for_class', models.ManyToManyField(help_text='выберете класс', to='application.classes')),
                ('school_lesson', models.ManyToManyField(help_text='выберете урок', to='application.lesson')),
            ],
        ),
    ]
