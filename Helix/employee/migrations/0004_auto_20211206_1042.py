# Generated by Django 3.2.8 on 2021-12-06 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_rename_time_type_timetype'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='end_Time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='schedule',
            name='start_Time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]