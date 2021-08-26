from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Product, Variation
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'category', 'modified_date','is_available')
    prepopulated_fields = {'slug': ('product_name',)}
    #list_display_links = ('email', 'first_name', 'last_name', 'username')
    #readonly_fields = ('last_login','date_joined')
    #ordering = ('-date_joined',)
    
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    
class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'variation_category', 'variation_value', 'is_active', 'created_date')
    list_editable = ('is_active',)
    list_filter = ('product', 'variation_category', 'variation_value')
    
admin.site.register(Product, ProductAdmin)
admin.site.register(Variation, VariationAdmin)