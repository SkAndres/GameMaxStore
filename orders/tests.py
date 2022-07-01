from django.test import TestCase

# Create your tests here.
from postal_code.utils import verify_cap
from postal_code.choices import StatusCAP
from django_countries import countries


country='UA'
cap = '123'
result = verify_cap(country, cap)
if result == StatusCAP.VALID:
    print("Perfect!")


