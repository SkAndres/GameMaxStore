from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Categories(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    category = models.ForeignKey(Categories, null=False, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=190)
    price = models.FloatField()
    description = models.TextField()
    quantity = models.IntegerField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
