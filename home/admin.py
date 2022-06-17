from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Categories)
class Categories(admin.ModelAdmin):
    list_display = ('id', 'category_name')
    list_filter = ['category_name']


@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = ('id', 'category', 'imagine', 'title', 'price', 'description', 'quantity')
    list_filter = ('category', 'title', 'price')


@admin.register(Order)
class Order(admin.ModelAdmin):
    list_display = ('id', 'customer', 'product', 'status')
    list_filter = ('id', 'customer', 'product', 'status')
