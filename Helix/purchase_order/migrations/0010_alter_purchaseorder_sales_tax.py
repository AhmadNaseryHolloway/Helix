# Generated by Django 3.2.8 on 2021-11-09 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase_order', '0009_auto_20211108_0755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='sales_Tax',
            field=models.DecimalField(blank=True, decimal_places=3, default=0.2, max_digits=4, null=True),
        ),
    ]