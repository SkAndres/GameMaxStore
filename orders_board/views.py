from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from orders.models import OrderItem
# Create your views here.


@login_required(login_url="account:log_in")
def order_board(request):
    order_items = OrderItem.objects.filter(user=request.user).order_by('-id')[:10]
    return render(request, 'my_orders.html', {'order_items': order_items})
