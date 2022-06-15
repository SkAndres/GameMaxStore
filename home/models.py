import django.contrib.auth
from django.db import models
import os
from django.contrib.auth.models import User

# Create your models here.


class MobilePhones(models.Model):
    imagine = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=190)
    price = models.FloatField()
    description = models.TextField()
    quantity = models.IntegerField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )
    customer = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    product = models.ForeignKey(MobilePhones, null=True, on_delete=models.CASCADE)
    data_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
