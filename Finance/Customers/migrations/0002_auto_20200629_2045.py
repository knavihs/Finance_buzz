# Generated by Django 3.0.7 on 2020-06-29 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Customers', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='username',
            new_name='user',
        ),
    ]