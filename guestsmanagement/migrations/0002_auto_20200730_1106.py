# Generated by Django 3.0.8 on 2020-07-30 05:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guestsmanagement', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Guests',
            new_name='Guest',
        ),
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
    ]
