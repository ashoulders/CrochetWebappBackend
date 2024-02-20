# Generated by Django 5.0.2 on 2024-02-20 18:32

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('date', models.DateField()),
                ('location', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='StockItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pattern_name', models.CharField(max_length=128)),
                ('standard_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='StockVariant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variant', models.CharField(max_length=256)),
                ('current_stock', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='markets.stockitem')),
            ],
        ),
        migrations.CreateModel(
            name='MarketStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('market', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='markets.market')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='markets.stockvariant')),
            ],
        ),
        migrations.CreateModel(
            name='ItemSold',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('number', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('market_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='markets.stockvariant')),
            ],
        ),
    ]
