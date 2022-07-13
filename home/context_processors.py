from django.shortcuts import render
from home.models import Categories, Product
from cart.cart import Cart
from GameMax.settings import GOOGLE_MAPS_API_KEY
from GameMax import settings



def categories(request):
    return {'categories': Categories.objects.all()}


def cart_items(request):
    return {'cart_items': Cart(request)}


def credentials(request):
    return {'credentials': settings.GOOGLE_MAPS_API_KEY}


def look_at_search(request):
    q = request.Get.get('q') if request.Get.get('q') != None else ''
    items = Product.objects.filter(title__name__icontains=q)
    return render(request, 'home.html', {'items': items})



