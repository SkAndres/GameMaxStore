from django.urls import path
from . import views

app_name = 'orders_board'

urlpatterns = [
    path('my_orders/', views.order_board, name='my_orders')
]
