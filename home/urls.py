from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='home'),
    path('product/<str:item_id>', views.product,  name='product'),

    path('related_prod/<str:item_id>', views.product,  name='related_prod'),
    path('chosen_category/<str:new_category_id>', views.chosen_category, name='chosen_category'),
    path('new_order/<str:devices_id>', views.new_order, name='new_order'),
]
