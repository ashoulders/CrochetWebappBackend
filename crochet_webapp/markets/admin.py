from django.contrib import admin
from markets.models import *

class MarketAdmin(admin.ModelAdmin):
    list_display = ['name', 'date', 'location']

class StockItemAdmin(admin.ModelAdmin):
    list_display = ['pattern_name', 'standard_price']

class StockVariantAdmin(admin.ModelAdmin):
    list_display = ['get_item_name', 'variant', 'current_stock']

    def get_item_name(self, obj):
        return obj.item.name
    
class MarketStockAdmin(admin.ModelAdmin):
    list_display = ['get_market_name', 'get_item_name', 'number']

    def get_market_name(self, obj):
        return obj.market.date

    def get_item_name(self, obj):
        return obj.item.name
    
class ItemSoldAdmin(admin.ModelAdmin):
    list_display = ['get_item_name', 'price', 'number']

    def get_item_name(self, obj):
        return obj.market_item.item.name

admin.site.register(Market, MarketAdmin)
admin.site.register(StockItem, StockItemAdmin)
admin.site.register(StockVariant, StockVariantAdmin)
admin.site.register(MarketStock, MarketStockAdmin)
admin.site.register(ItemSold, ItemSoldAdmin)
