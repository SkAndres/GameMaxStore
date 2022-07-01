from django.contrib import admin
from .models import Order, OrderItem
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields
# Register your models here.


@admin.register(Order)
class Order(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'phone_number', 'cap')
    list_filter = ('id', 'first_name', 'last_name', 'email', 'phone_number', 'address')
    formfield_overrides = {
        map_fields.AddressField: {'widget': map_widgets.GoogleMapsAddressWidget},
    }


@admin.register(OrderItem)
class OrderItem(admin.ModelAdmin):
    list_display = ('id', 'order', 'product', 'total_price')
    list_filter = ('id', 'order', 'product', 'total_price')

