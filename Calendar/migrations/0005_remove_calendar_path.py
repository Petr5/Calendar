# Generated by Django 3.2.3 on 2021-05-28 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Calendar', '0004_calendar_path'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calendar',
            name='path',
        ),
    ]