# Generated by Django 3.2.8 on 2021-11-01 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BOM', '0002_alter_bom_item_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bom',
            name='quantity',
            field=models.FloatField(default=0),
        ),
    ]
