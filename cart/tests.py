from django.test import TestCase
from decimal import Decimal

# Create your tests here.

x = {'price': 0.3,
     'quantity': 2}

print(x['price'] * x['quantity'])



number = Decimal('0.1')

number = number * 3
print(number)