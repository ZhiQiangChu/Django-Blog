# Generated by Django 2.0.4 on 2018-09-09 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0003_auto_20180909_2049'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='age',
        ),
    ]
