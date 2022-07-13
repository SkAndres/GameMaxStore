from django.db.models import Q
from django.shortcuts import render
from .models import Product
from cart.forms import CartAddProductForm


# Create your views here.


def home(request):
    items = Product.objects.all()
    query = request.GET.get('q')
    if query:
        items = Product.objects.filter(
            Q(title__icontains=query) |
            Q(price__icontains=query)
        )
    return render(request, 'home.html', {'items': items})


def products(request, item_id):
    device = Product.objects.get(pk=item_id)
    form = CartAddProductForm()
    rel_prods = Product.objects.all()
    return render(request, 'product.html', {'device': device, 'rel_prods': rel_prods, 'form': form})


def chosen_category(request, category_id):
    by_category = Product.objects.filter(category=category_id)
    return render(request, 'category.html', {'by_category': by_category})



