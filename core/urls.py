from django.urls import path
from . import views

urlpatterns = [
    path('restaurants/', views.restaurant_list, name='restaurant_list'),
    path('restaurants/<int:restaurant_id>/dishes/', views.dish_list, name='dish_list'),
    path('order/<int:dish_id>/', views.order_dish, name='order_dish'),
    path('orders/', views.orders, name='orders')
]