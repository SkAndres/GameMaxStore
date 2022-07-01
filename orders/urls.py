from django.urls import path, re_path, include
from . import views

app_name = 'orders'

urlpatterns = [
    path('', views.order_confirmation, name='order_confirmation'),
]
