# Generated by Django 3.2.8 on 2021-11-08 07:55

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('purchase_order', '0008_alter_purchaseorder_order_number_unique_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='delivery_Required_Date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='order_Date',
            field=models.DateField(default=datetime.date.today, null=True),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='supplier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='purchase_order.suppliers'),
        ),
    ]
