# Generated by Django 4.0.7 on 2022-09-19 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='slug',
        ),
    ]
