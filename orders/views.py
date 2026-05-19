from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem
from shop.models import Product

# Create your views here.

# @login_required
# def create_order(request):
#     cart = request.session.get('cart', {})

#     if not cart:
#         return redirect('cart:cart_detail')

#     order = Order.objects.create(user=request.user)

#     for product_id, item in cart.items():
#         product = Product.objects.get(id=product_id)

#         if isinstance(item, dict):
#             quantity = item.get('quantity', 1)
#         else:
#             quantity = item

#         OrderItem.objects.create(
#             order=order,
#             product=product,
#             price=product.price,
#             quantity=quantity
#         )

#     request.session['cart'] = {}
#     request.session.modified = True

#     #return redirect('orders:user_orders')
#     return redirect('orders:order_success')


@login_required
def create_order(request):
    cart = request.session.get('cart', {})

    if not cart:
        return redirect('cart:cart_detail')

    product_ids = cart.keys()
    products = Product.objects.filter(id__in=product_ids)
    products_dict = {str(product.id): product for product in products}

    order = Order.objects.create(user=request.user)

    for product_id, item in cart.items():
        product = products_dict.get(str(product_id))

        if not product:
            continue

        if isinstance(item, dict):
            quantity = item.get('quantity', 1)
        else:
            quantity = item

        OrderItem.objects.create(
            order=order,
            product=product,
            price=product.price,
            quantity=quantity
        )

    request.session['cart'] = {}
    request.session.modified = True

    return redirect('orders:order_success')


@login_required
def user_orders(request):
    # orders = Order.objects.filter(user=request.user).order_by('-created_at')
    orders = (
        Order.objects
        .filter(user=request.user)
        .prefetch_related('items__product')
        .order_by('-created_at')
    )

    return render(request, 'orders/user_orders.html', {
        'orders': orders
    })


@login_required
def order_success(request):
    return render(request, 'orders/order_success.html')
