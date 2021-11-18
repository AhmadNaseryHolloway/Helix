# Generated by Django 3.2.8 on 2021-10-25 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_Name', models.CharField(max_length=120, primary_key=True, serialize=False)),
                ('addresss', models.TextField()),
                ('phone', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Customers',
            },
        ),
    ]
