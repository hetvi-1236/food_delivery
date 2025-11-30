from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('restaurants/', views.restaurant_list, name='restaurant_list'),
    path('restaurants/<int:restaurant_id>/dishes/', views.dish_list, name='dish_list'),
    path('order/<int:dish_id>/', views.order_dish, name='order_dish'),
    path('orders/', views.orders, name='orders'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]