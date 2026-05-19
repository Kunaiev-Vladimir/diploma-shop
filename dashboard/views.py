from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from django.shortcuts import render

from orders.models import Order
from shop.models import Product


@staff_member_required
def dashboard_view(request):
    orders_count = Order.objects.count()
    products_count = Product.objects.count()
    users_count = User.objects.count()

    # recent_orders = Order.objects.order_by('-id')[:5]
    recent_orders = Order.objects.order_by('-id')

    context = {
        'orders_count': orders_count,
        'products_count': products_count,
        'users_count': users_count,
        'recent_orders': recent_orders,
    }

    return render(request, 'dashboard/dashboard.html', context)
