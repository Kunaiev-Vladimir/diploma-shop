from django.shortcuts import render, redirect, get_object_or_404
from shop.models import Product

# Create your views here.

def cart_detail(request):
    cart = request.session.get('cart', {})
    products = []
    total_price = 0

    for product_id, quantity in cart.items():
        product = Product.objects.get(id=product_id)
        product.total_price = product.price * quantity
        product.quantity = quantity
        total_price += product.total_price
        products.append(product)

    return render(request, 'cart/cart_detail.html', {
        'products': products,
        'total_price': total_price
    })


def cart_add(request, product_id):
    cart = request.session.get('cart', {})

    if str(product_id) in cart:
        cart[str(product_id)] += 1
    else:
        cart[str(product_id)] = 1

    request.session['cart'] = cart
    request.session.modified = True

    return redirect(request.META.get('HTTP_REFERER', 'shop:product_list'))


def cart_remove(request, product_id):
    cart = request.session.get('cart', {})

    if str(product_id) in cart:
        del cart[str(product_id)]

    request.session['cart'] = cart

    return redirect('cart:cart_detail')

def update_cart(request, product_id):
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        cart = request.session.get('cart', {})

        if str(product_id) in cart:
            cart[str(product_id)] = quantity

        request.session['cart'] = cart

    return redirect('cart:cart_detail')