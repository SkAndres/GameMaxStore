from django.contrib import admin
from .models import Order, OrderItem
# Register your models here.


@admin.register(Order)
class Order(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'phone_number', 'address')
    list_filter = ('id', 'first_name', 'last_name', 'email', 'phone_number', 'address')


@admin.register(OrderItem)
class OrderItem(admin.ModelAdmin):
    list_display = ('id', 'order', 'product', 'total_price')
    list_filter = ('id', 'order', 'product', 'total_price')
