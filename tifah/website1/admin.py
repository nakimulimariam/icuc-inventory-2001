from django.contrib import admin

from .models import EquipmentCategory, Product, Transaction

class EquipmentCategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'date_created')
    list_filter = ('date_created',)
    search_fields = ('category_name',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('category_id', 'product_name', 'unit_price', 'sale_price', 'available_stock', 'unit_measure', 'date_updated')
    list_filter = ('date_updated',)
    search_fields = ('category_id', 'product_name')
    
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'transaction_type', 'stock_taken', 'transaction_amount', 'transaction_date')
    list_filter = ('transaction_date',)
    search_fields = ('product_id', 'transaction_type')

admin.site.register(EquipmentCategory, EquipmentCategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Transaction, TransactionAdmin)

