# Generated by Django 3.2.8 on 2021-11-05 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase_order', '0007_alter_purchaseorder_fao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='order_Number_Unique_ID',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]