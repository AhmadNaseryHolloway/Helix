# Generated by Django 3.2.8 on 2021-11-01 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_auto_20211029_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockitems',
            name='net_Cost_Each',
            field=models.FloatField(default=0),
        ),
    ]
