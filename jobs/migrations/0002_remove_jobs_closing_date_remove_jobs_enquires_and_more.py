# Generated by Django 4.0.7 on 2022-09-03 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobs',
            name='closing_date',
        ),
        migrations.RemoveField(
            model_name='jobs',
            name='enquires',
        ),
        migrations.RemoveField(
            model_name='jobs',
            name='experience',
        ),
        migrations.RemoveField(
            model_name='jobs',
            name='note',
        ),
        migrations.RemoveField(
            model_name='jobs',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='jobs',
            name='seoDescription',
        ),
        migrations.RemoveField(
            model_name='jobs',
            name='seoKeywords',
        ),
        migrations.RemoveField(
            model_name='jobs',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='jobs',
            name='summary',
        ),
        migrations.RemoveField(
            model_name='jobs',
            name='type',
        ),
        migrations.AlterField(
            model_name='jobs',
            name='category',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='company',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='date_posted',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='salary',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Company',
        ),
    ]
