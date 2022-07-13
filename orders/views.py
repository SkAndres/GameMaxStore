from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import OrderForm
from cart.cart import Cart
from .models import OrderItem
from home.models import Product
from .tasks import NewTask
# Create your views here.


@login_required(login_url="account:log_in")
def order_confirmation(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order_form = form.save()
            for item in cart:
                order = OrderItem.objects.create(user=request.user,
                                                 order=order_form,
                                                 product=item['product'],
                                                 price=cart.get_total_price(),
                                                 quantity=item['quantity'])
                if order:
                    NewTask.order_task(order_form, order, cart)

                # updating quantity
                product = Product.objects.get(title=item['product'])
                product.quantity -= item['quantity']
                product.save()

            # clear the cart
            cart.clear()
            return redirect('home:home')
    else:
        form = OrderForm()
    return render(request, "order_confirm.html", {"form": form, 'cart': cart})