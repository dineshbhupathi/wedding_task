# Generated by Django 3.0.8 on 2020-07-30 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guestsmanagement', '0004_purchase_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
