from django.shortcuts import render
from .models import Product, Order
from cart.forms import CartAddProductForm

# Create your views here.


def index(request):
    items = Product.objects.all().order_by('-title')
    form = CartAddProductForm()
    return render(request, 'home.html', {'items': items, 'form': form})


def product(request, item_id):
    device = Product.objects.get(pk=item_id)
    form = CartAddProductForm()
    rel_prods = Product.objects.all()
    return render(request, 'product.html', {'device': device, 'rel_prods': rel_prods, 'form': form})


def chosen_category(request, category_id):
    by_category = Product.objects.filter(category=category_id)
    return render(request, 'category.html', {'by_category': by_category})


def new_order(request, devices_id):
    products = Product.objects.get(pk=devices_id)
    order = Order(request)
    order.add(product=products)
