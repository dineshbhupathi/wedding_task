# Generated by Django 3.0.8 on 2020-07-30 05:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('brand', models.CharField(max_length=225)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('in_stock_quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Guests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('gift_products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guestsmanagement.Products')),
            ],
        ),
    ]
