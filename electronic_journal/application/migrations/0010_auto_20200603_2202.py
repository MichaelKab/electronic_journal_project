# Generated by Django 3.0.6 on 2020-06-03 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0009_auto_20200603_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='teacher',
            field=models.CharField(choices=[], default='', help_text='учитель', max_length=100),
        ),
    ]
