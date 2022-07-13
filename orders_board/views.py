from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from orders.models import OrderItem, Order
from home.models import Product
from django.db.models import Sum

# Create your views here.


@login_required(login_url="account:log_in")
def order_board(request):
    order_items = OrderItem.objects.filter(user=request.user).order_by('-id')
    return render(request, 'my_orders.html', {'order_items': order_items})
