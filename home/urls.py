from django.urls import path
from . import views
from . import context_processors

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<str:item_id>', views.products, name='product'),
    path('related_prod/<str:item_id>', views.products, name='related_prod'),
    path('chosen_category/<str:new_category_id>', views.chosen_category, name='chosen_category'),
    path('category/<str:category_id>', views.chosen_category, name='chosen_category'),

]
