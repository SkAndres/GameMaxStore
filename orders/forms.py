from django import forms
from .models import Order
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from phonenumber_field.formfields import PhoneNumberField
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from postal_code.utils import verify_cap
from postal_code.choices import StatusCAP
from django.forms import ModelForm
from localflavor.ua.forms import UAPostalCodeField
from address.forms import AddressField, AddressWidget



class OrderForm(ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'First name',
                'style': 'width: 300px',
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'text',
        'class': 'form-control',
        'placeholder': 'Last name',
        'style': 'width: 300px',
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'type': 'text',
        'class': 'form-control',
        'placeholder': 'Email',
        'style': 'width: 300px',

    }))
    phone_number = PhoneNumberField(widget=PhoneNumberPrefixWidget(initial='US', attrs={'class': 'form-control'}))
    country = CountryField().formfield(
        widget=CountrySelectWidget(
            attrs={'class': 'form-control',
                   'style': 'width: 300px',
                   }))
    cap = UAPostalCodeField(widget=forms.TextInput(attrs={
        'type': 'text',
        'class': 'form-control',
        'style': 'width: 150px',
    }))
    address = AddressField(widget=AddressWidget(attrs={'class': 'Autocomplete'}))

    class Meta:
        model = Order
        fields = ("first_name", "last_name", "email", 'phone_number', 'country', 'cap', 'address')
