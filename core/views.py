from django.shortcuts import render, redirect
from .models import Restaurant, Dish, Order
from django.contrib.auth.decorators import login_required

from django.db.models import Q

def restaurant_list(request):
    query = request.GET.get('q')
    if query:
        restaurants = Restaurant.objects.filter(
            Q(name__icontains=query) | Q(dishes__name__icontains=query)
        ).distinct()
    else:
        restaurants = Restaurant.objects.all()
    return render(request, 'core/restaurant_list.html', {'restaurants': restaurants})

def dish_list(request, restaurant_id):
    dishes = Dish.objects.filter(restaurant_id=restaurant_id)
    return render(request, 'core/dish_list.html', {'dishes': dishes, 'restaurant_id': restaurant_id})

@login_required
def order_dish(request, dish_id):
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        Order.objects.create(user=request.user, dish_id=dish_id, quantity=quantity)
        return redirect('orders')
    dish = Dish.objects.get(id=dish_id)
    return render(request, 'core/order_dish.html', {'dish': dish})

@login_required
def orders(request):
    user_orders = Order.objects.filter(user=request.user)
    return render(request, 'core/orders.html', {'orders': user_orders})

def landing(request):
    return render(request, 'core/landing.html')

