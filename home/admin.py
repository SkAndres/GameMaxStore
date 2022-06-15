from django.contrib import admin
from .models import MobilePhones, Order


# Register your models here.

@admin.register(MobilePhones)
class MobilePhones(admin.ModelAdmin):
    list_display = ('id', 'imagine', 'title', 'price', 'description', 'quantity')
    list_filter = ('imagine', 'title', 'price', 'description', 'quantity')


@admin.register(Order)
class MobilePhones(admin.ModelAdmin):
    list_display = ('id', 'customer', 'product', 'status')
    list_filter = ('id', 'customer', 'product', 'status')
