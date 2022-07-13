from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import OrderForm
from cart.cart import Cart
from .models import OrderItem
from home.models import Product
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
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
                # updating quantity
                product = Product.objects.get(title=item['product'])
                product.quantity -= item['quantity']
                product.save()

                # sending an email with a confirmation
                subject = 'New Order'
                html_message = render_to_string("email_template.html",
                                                {'order_form': order_form, 'order': order, 'cart': cart})
                plain_message = strip_tags(html_message)
                send_mail(subject, plain_message, settings.EMAIL_HOST_USER, [order_form.email],
                          html_message=html_message)
            # clear the cart
            cart.clear()
            return redirect('home:home')
    else:
        form = OrderForm()
    return render(request, "order_confirm.html", {"form": form, 'cart': cart})