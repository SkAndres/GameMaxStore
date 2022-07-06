from django.db import models
from home.models import Product
from cart.cart import Cart
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField
from address.models import AddressField
from places.fields import PlacesField
from django_google_maps import fields as map_fields
from django_google_maps.fields import AddressField, GeoLocationField
from places.fields import PlacesField


class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=125)
    phone_number = PhoneNumberField()
    address = models.CharField(max_length=300)
    exact_address = models.CharField(max_length=70, null=True)
    city = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=100, null=True)
    post_code = models.CharField(max_length=6, null=True)
    country = models.CharField(max_length=300, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name


class OrderItem(models.Model):
    order = models.ForeignKey(Order, null=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    quantity = models.PositiveIntegerField(default=1)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
