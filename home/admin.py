from django.contrib import admin
from .models import Categories, Product


# Register your models here.
@admin.register(Categories)
class Categories(admin.ModelAdmin):
    list_display = ('id', 'category_name')
    list_filter = ['category_name']


@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = ('id', 'category', 'image', 'title', 'price', 'description', 'quantity')
    list_filter = ('category', 'title', 'price')



