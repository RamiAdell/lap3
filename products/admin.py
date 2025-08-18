from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'price', 'instock', 'created_at')
    list_filter = ('created_at', 'instock')
    search_fields = ('name', 'code', 'description')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)
