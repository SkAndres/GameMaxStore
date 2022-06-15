from django.shortcuts import render, redirect
from .models import MobilePhones, Order
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    items = MobilePhones.objects.all()
    return render(request, 'home.html', {'items': items})


def product(request, item_id):
    devices = MobilePhones.objects.get(pk=item_id)
    rel_prods = MobilePhones.objects.all()
    return render(request, 'product.html', {'devices': devices, 'rel_prods': rel_prods})


def related_products(request):
    rel_prods = MobilePhones.objects.all()
    return render(request, 'product.html', {'rel_prods': rel_prods})


def new_order(request, devices_id):
    products = MobilePhones.objects.get(id=devices_id)
    order = Order(request)
    order.add(product=products)