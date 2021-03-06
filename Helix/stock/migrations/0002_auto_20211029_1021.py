# Generated by Django 3.2.8 on 2021-10-29 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='discount_Percentage',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='stockitems',
            name='branches',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='employee.branch'),
        ),
        migrations.AlterField(
            model_name='stockitems',
            name='line_Total_Sum',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='stockitems',
            name='long_Description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stockitems',
            name='net_Cost_Each',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='stockitems',
            name='stock_Balance_Notts',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stockitems',
            name='stock_Level_Min',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stockitems',
            name='stock_Level_Status',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stockitems',
            name='stock_Location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='stock.stocklocation'),
        ),
        migrations.AlterField(
            model_name='stocklocation',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stocklog',
            name='branch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='employee.branch'),
        ),
        migrations.AlterField(
            model_name='stocklog',
            name='branch_Location',
            field=models.CharField(blank=True, choices=[('telford', 'Telford'), ('nottingham', 'Nottingham')], max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='stocklog',
            name='calender_Info',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stocklog',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stocklog',
            name='qty_Added',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='stocklog',
            name='qty_Removed',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='stocklog',
            name='value_Removed',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
    ]
