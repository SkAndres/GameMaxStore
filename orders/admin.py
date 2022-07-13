from .models import Order, OrderItem
from django.contrib import admin

# Register your models here.


@admin.register(Order)
class Order(admin.ModelAdmin):
    list_display = ('id','first_name', 'last_name', 'email', 'phone_number',
                    'address', 'country', 'exact_address', 'city', 'state',
                    'post_code', 'country')
    list_filter = ('first_name', 'last_name', 'email', 'phone_number',
                   'address', 'country', 'exact_address', 'city', 'state',
                   'post_code', 'country')


@admin.register(OrderItem)
class OrderItem(admin.ModelAdmin):
    list_display = ('id', 'user', 'order', 'product', 'quantity', 'price')
    list_filter = ('id', 'user', 'order', 'product', 'quantity', 'price')


