# Generated by Django 4.0.7 on 2022-10-07 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0006_delete_company_job_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract_Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract_type', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
