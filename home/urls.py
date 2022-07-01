from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='home'),
    path('product/<str:item_id>', views.product,  name='product'),
    path('related_prod/<str:item_id>', views.product,  name='related_prod'),
    path('chosen_category/<str:new_category_id>', views.chosen_category, name='chosen_category'),
    path('category/<str:category_id>', views.chosen_category, name='chosen_category')
]
