from django.contrib import admin
from .models import Product

class DataBackEndFCO(admin.ModelAdmin):
    list_display = (
                    'sku',
                    'price',
                    'vat_type',
                    'description',
                   )
    search_fields = (
                    'sku',
                    'price',
                    'vat_type',
                    )
    list_filter = (
                    'sku',
                    'price',
                    'vat_type',
                  )
    
admin.site.register(Product, DataBackEndFCO)