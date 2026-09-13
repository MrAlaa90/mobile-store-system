from django.contrib import admin
from .models import License, Device, Customer, Inventory, Sale, Repair

@admin.register(License)
class LicenseAdmin(admin.ModelAdmin):
    list_display = ('license_key', 'user', 'valid_until', 'status')
    search_fields = ('license_key', 'user__username')

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('hardware_hash', 'license', 'last_seen')

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'created_at')
    search_fields = ('name', 'phone')

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'model', 'purchase_price', 'sale_price', 'stock')
    search_fields = ('name', 'brand', 'model')

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ('id', 'total_amount', 'profit', 'created_at', 'synced')
    list_filter = ('synced', 'created_at')

@admin.register(Repair)
class RepairAdmin(admin.ModelAdmin):
    list_display = ('device_info', 'customer', 'cost', 'payment', 'status', 'synced')
    list_filter = ('status', 'synced')
