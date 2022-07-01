from django.shortcuts import render, redirect
from .forms import OrderForm
from cart.cart import Cart
# Create your views here.


def order_confirmation(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:home')
    else:
        form = OrderForm()
    return render(request, "confirmation.html", {"form": form, 'cart': cart})
