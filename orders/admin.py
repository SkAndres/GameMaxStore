from django.contrib import admin
from .models import Order, OrderItem
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields
import json
from django.contrib import admin
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields

# Register your models here.


@admin.register(Order)
class Order(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number',
                    'address', 'country', 'exact_address', 'city', 'state',
                    'post_code', 'country')
    list_filter = ('first_name', 'last_name', 'email', 'phone_number',
                   'address', 'country', 'exact_address', 'city', 'state',
                   'post_code', 'country')


@admin.register(OrderItem)
class OrderItem(admin.ModelAdmin):
    list_display = ('id', 'order', 'product', 'quantity', 'price')
    list_filter = ('id', 'order', 'product', 'quantity', 'price')


