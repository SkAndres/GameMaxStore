from django.shortcuts import render
from .forms import OrderForm
from address.models import Address
from django.conf import settings
# Create your views here.


def order_confirmation(request):
    addresses = Address.objects.all()
    success = False

    if settings.GOOGLE_API_KEY:
        google_api_key_set = True
    else:
        google_api_key_set = False

    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            success = True
            form.save()
    else:
        form = OrderForm(initial={"address": Address.objects.last()})

    context = {
        "form": form,
        "google_api_key_set": google_api_key_set,
        "success": success,
        "addresses": addresses,
    }

    return render(request, 'confirmation.html', {'context': context})
