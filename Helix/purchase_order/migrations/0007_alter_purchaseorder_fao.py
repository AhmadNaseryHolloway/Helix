# Generated by Django 3.2.8 on 2021-11-04 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase_order', '0006_alter_purchaseorder_order_number_unique_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='fao',
            field=models.CharField(blank=True, default='Holloway Controls', max_length=120, null=True),
        ),
    ]
