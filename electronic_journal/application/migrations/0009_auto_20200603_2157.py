# Generated by Django 3.0.6 on 2020-06-03 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0008_auto_20200603_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='student',
            field=models.CharField(choices=[], default='', help_text='ученик', max_length=100),
        ),
    ]
