from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from home.models import Product
from .cart import Cart
from .forms import CartAddProductForm
from django.contrib import messages

# Create your views here.
import json


@login_required(login_url="account:log_in")
def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        product = Product.objects.get(title=item['product'])
        if product.quantity > item['quantity'] or product.quantity == item['quantity']:
            item['update_quantity_form'] = CartAddProductForm(
                initial={'quantity': item['quantity'],
                         'update': True})
        else:
            del item['quantity']
            item['quantity'] = product.quantity
            print(item['quantity'])
            item['update_quantity_form'] = CartAddProductForm(
                initial={'quantity': item['quantity'],
                         'update': True})
    return render(request, 'cart/detail.html', {'cart': cart})


@require_POST
@login_required(login_url="account:log_in")
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        if product.quantity > cd['quantity'] or product.quantity == cd['quantity']:
            if cd['update']:
                cart.add(product=product,
                         quantity=cd['quantity'],
                         update_quantity=cd['update'])
                return redirect(request.META.get('HTTP_REFERER'))
            else:
                cart.add(product=product,
                         quantity=cd['quantity'],
                         update_quantity=cd['update'])
                messages.success(request, 'Product is successfully added to the cart')
                return redirect(request.META.get('HTTP_REFERER'))
        elif product.quantity <= 1:
            messages.error(request, 'Sorry, this item is not available')
            return redirect(request.META.get('HTTP_REFERER'))
        elif product.quantity <= cd['quantity']:
            messages.error(request, f'quantity error, max available quantity this item is {product.quantity}')
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request, 'Sorry, this item is not available')
            return redirect(request.META.get('HTTP_REFERER'))


@require_POST
@login_required(login_url="account:log_in")
def cart_add_common(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    if product.quantity == 0:
        messages.error(request, 'Sorry, this item is not available')
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        cart.add(product=product, quantity=1, update_quantity=False)
        messages.success(request, 'Product is successfully added to the cart')
        return redirect(request.META.get('HTTP_REFERER'))


@login_required(login_url="account:log_in")
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')
