from home.models import Categories
from cart.cart import Cart


def categories(request):
    return {'categories': Categories.objects.all()}


def cart_items(request):
    return {'cart_items': Cart(request)}
