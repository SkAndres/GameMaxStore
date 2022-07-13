import requests
from django.core.validators import MinValueValidator
from django.db import models


from home.models import Product
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User


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
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, null=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user



