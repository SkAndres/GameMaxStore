from django.shortcuts import render
from .models import Product, Order

# Create your views here.


def index(request):
    items = Product.objects.all()
    return render(request, 'home.html', {'items': items})


def product(request, item_id):
    devices = Product.objects.get(pk=item_id)
    rel_prods = Product.objects.all()
    return render(request, 'product.html', {'devices': devices, 'rel_prods': rel_prods})


def chosen_category(request, new_category_id):
    by_category = Product.objects.get(id=new_category_id)
    return render(request, 'category.html', {'by_category': by_category})


def new_order(request, devices_id):
    products = Product.objects.get(id=devices_id)
    order = Order(request)
    order.add(product=products)
