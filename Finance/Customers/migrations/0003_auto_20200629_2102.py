# Generated by Django 3.0.7 on 2020-06-29 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customers', '0002_auto_20200629_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='companies_invested',
            field=models.CharField(max_length=20),
        ),
        migrations.DeleteModel(
            name='Stocks',
        ),
    ]