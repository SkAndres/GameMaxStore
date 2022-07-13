from django import forms
from .models import Order
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from phonenumber_field.formfields import PhoneNumberField
from django.forms import ModelForm


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
    phone_number = PhoneNumberField(widget=PhoneNumberPrefixWidget(initial='US', attrs={'class': 'form-control',
                                                                                        'style': 'width: 300px',}))
    address = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'text',
        'class': 'form-control',
        'id': 'ship-address',
        'name': 'ship-address',
        'style': 'width: 300px',
        'placeholder': 'Street address'}))

    exact_address = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'text',
        'class': 'form-control',
        'id': 'address2',
        'name': 'address2',
        'style': 'width: 300px',
        'placeholder': 'Apartment, unit, suite, or floor'}))

    city = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'text',
        'class': 'form-control',
        'id': 'locality',
        'name': 'locality',
        'style': 'width: 300px',
        'placeholder': 'City'}))

    state = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'text',
        'class': 'form-control',
        'id': 'state',
        'name': 'state',
        'style': 'width: 300px',
        'placeholder': 'State/Province'}))

    post_code = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'text',
        'class': 'form-control',
        'id': 'postcode',
        'name': 'postcode',
        'style': 'width: 300px',
        'placeholder': 'Postal code'}))

    country = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'text',
        'class': 'form-control',
        'id': 'country',
        'name': 'country',
        'style': 'width: 300px',
        'placeholder': 'Country/Region'}))


    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'phone_number',
                  'address', 'country', 'exact_address', 'city', 'state',
                  'post_code', 'country']
