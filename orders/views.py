from django.shortcuts import render, redirect
from .forms import OrderForm
from cart.cart import Cart
from django.conf import settings
from .models import OrderItem
from home.models import Product
# Create your views here.


def order_confirmation(request):
    cart = Cart(request)
    print(cart)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])

                product = Product.objects.get(title=item['product'])
                product.quantity -= item['quantity']
                product.save()
            # clear the cart
            cart.clear()
            return redirect('home:home')
    else:
        form = OrderForm()
    return render(request, "confirmation.html", {"form": form, 'cart': cart, 'google_api_key': settings.GOOGLE_API_KEY})


