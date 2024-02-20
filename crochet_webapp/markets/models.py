from django.db import models
from django.core.validators import MinValueValidator

class Market(models.Model):
    name = models.CharField(max_length=128)
    date = models.DateField()
    location = models.CharField(max_length=128)

class StockItem(models.Model):
    pattern_name = models.CharField(max_length=128)
    standard_price = models.DecimalField(max_digits=5, decimal_places=2)
    picture = models.ImageField(blank=True, null=True)

# e.g. colour 
class StockVariant(models.Model):
    item = models.ForeignKey(StockItem, on_delete=models.CASCADE)
    variant = models.CharField(max_length=256)
    current_stock = models.IntegerField(default=0, validators=[MinValueValidator(0)])

class MarketStock(models.Model):
    market = models.ForeignKey(Market, on_delete=models.CASCADE)
    item = models.ForeignKey(StockVariant, on_delete=models.CASCADE)
    number = models.IntegerField(validators=[MinValueValidator(0)])

# this table exists as price may differ per item sold, even if it is the same item
# for example in a deal e.g 2 for £10
class ItemSold(models.Model):
    market_item = models.ForeignKey(StockVariant, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    number = models.IntegerField(validators=[MinValueValidator(0)])
