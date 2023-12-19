from django.contrib import admin

from django.contrib import admin

# Register your models here.
from .models import User, Product


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'telegram_id')
    search_fields = ('telegram_id', 'username')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'price', 'category_name')
    search_fields = ('product_name', 'category_name')


admin.site.register(User)
admin.site.register(Product)
