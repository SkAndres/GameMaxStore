from decimal import Decimal
from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect
from requests import request

from home.models import Product


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity, update_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'price': str(product.price)}
        elif product_id in self.cart:
            if product.quantity > self.cart[product_id]['quantity'] \
                    or product.quantity == self.cart[product_id]['quantity']:
                self.cart[product_id] = {'quantity': product.quantity,
                                         'price': str(product.price)}
            else:
                messages.error(request, f'quantity error, max available quantity this item is {product.quantity}')
                return redirect(request.META.get('HTTP_REFERER'))
        if update_quantity:
            if product.quantity > self.cart[product_id]['quantity'] \
                    or product.quantity == self.cart[product_id]['quantity']:
                self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
        self.save()

    def __iter__(self):
        product_ids = self.cart.keys()
        # get the product objects and add them to the cart
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in
                   self.cart.values())

    def clear(self):
        # remove cart from session
        del self.session[settings.CART_SESSION_ID]
        self.save()

    def save(self):
        self.session.modified = True


