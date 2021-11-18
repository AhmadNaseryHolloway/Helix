from django.contrib import admin

from .models import StockCategory, StockItems, StockLocation, StockManufacturer, StockOwner, StockLog, Products

# Register your models here.

admin.site.register(StockOwner)
admin.site.register(StockCategory)
admin.site.register(StockItems)
admin.site.register(StockLocation)
admin.site.register(StockManufacturer)
admin.site.register(StockLog)
admin.site.register(Products)