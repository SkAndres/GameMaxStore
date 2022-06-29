from django import forms
from .models import Order
from address.forms import AddressField


class OrderForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'First name',
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'text',
        'class': 'form-control',
        'placeholder': 'Last name',
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'type': 'text',
        'class': 'form-control',
        'placeholder': 'Email',
    }))
    address = AddressField(widget=forms.TextInput(attrs={
        'type': 'text',
        'class': 'form-control',
        'placeholder': 'First name"',
    }))

    class Meta:
        model = Order
        fields = ("first_name", "last_name", "email", "phone_number", "address")
