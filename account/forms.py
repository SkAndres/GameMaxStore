from django import forms
from django.contrib.auth.models import User

from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm, UserCreationForm
from django.core.exceptions import ObjectDoesNotExist


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
                'type': 'text',
                'class': 'form-control form-control-lg',
                'placeholder': 'Username',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
                'type': 'password',
                'class': 'form-control form-control-lg',
                'placeholder': 'Password',
                'style': 'margin-left: 0px;',
                'id': 'typeEmailX',
                'for': 'typeEmailX'
    }))


class UserPasswordResetForm(PasswordResetForm):
    email = forms.CharField(widget=forms.TextInput(attrs={
                'type': 'email',
                'class': 'form-control form-control-lg',
                'placeholder': 'Email',
                'style': 'margin-left: 0px;',
    }))


class UserSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={
                'type': 'email',
                'class': 'form-control form-control-lg',
                'placeholder': 'Password',
                'style': 'margin-left: 0px;',
    })),
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'type': 'email',
        'class': 'form-control form-control-lg',
        'placeholder': 'Confirm password',
        'style': 'margin-left: 0px;',
    }))


class CustomUserCreationForm(UserCreationForm):

    username = forms.CharField(max_length=75, widget=forms.TextInput(attrs={
        'type': 'username',
        'class': 'form-control form-control-lg',
        'placeholder': 'Username',
        'style': 'margin-left: 0px;',
    }))

    first_name = forms.CharField(max_length=75, widget=forms.TextInput(attrs={
        'class': 'form-control form-control-lg',
        'placeholder': 'First name',
        'style': 'margin-left: 0px;',
    }))

    last_name = forms.CharField(max_length=75, widget=forms.TextInput(attrs={
        'class': 'form-control form-control-lg',
        'placeholder': 'Last name',
        'style': 'margin-left: 0px;',
    }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'type': 'email',
        'class': 'form-control form-control-lg',
        'placeholder': 'Email',
        'style': 'margin-left: 0px;',
    }))

    password1 = forms.CharField(min_length=5, max_length=75, widget=forms.PasswordInput(attrs={
                'type': 'password',
                'class': 'form-control form-control-lg',
                'placeholder': 'Password',
                'style': 'margin-left: 0px;',
    }))

    password2 = forms.CharField(min_length=5, max_length=75, widget=forms.PasswordInput(attrs={
        'type': 'password',
        'class': 'form-control form-control-lg',
        'placeholder': 'Confirm password',
        'style': 'margin-left: 0px;',
    }))

    def username_clean(self):
        username = self.cleaned_data['username'].lower()
        check = User.objects.filter(username=username)
        if check.count():
            raise forms.ValidationError("User Already Exist")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        check = User.objects.filter(email=email)
        if check:
            raise forms.ValidationError("This email already exist!")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 != password2:
            raise forms.ValidationError("The passwords don't match!")
        return password1

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")
