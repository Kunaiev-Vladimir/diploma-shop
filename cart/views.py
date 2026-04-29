from django.shortcuts import render, redirect, get_object_or_404
from shop.models import Product
from django.http import JsonResponse

# Create your views here.

def cart_detail(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0

    for product_id, item in cart.items():
        product = get_object_or_404(Product, id=product_id)

        quantity = item['quantity']
        item_total = product.price * quantity

        cart_items.append({
            'product': product,
            'quantity': quantity,
            'total': item_total,
        })

        total += item_total

    return render(request, 'cart/cart_detail.html', {
        'cart_items': cart_items,
        'total': total,
    })


#def cart_add(request, product_id):
    #cart = request.session.get('cart', {})

    #if str(product_id) in cart:
        #cart[str(product_id)] += 1
    #else:
        #cart[str(product_id)] = 1

    #request.session['cart'] = cart
    #request.session.modified = True

    #return redirect(request.META.get('HTTP_REFERER', 'shop:product_list'))
def cart_add(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    cart = request.session.get('cart', {})

    product_id_str = str(product.id)

    if product_id_str in cart:
        cart[product_id_str]['quantity'] += 1
    else:
        cart[product_id_str] = {
            'quantity': 1,
            'price': str(product.price),
        }

    request.session['cart'] = cart
    request.session.modified = True

    cart_count = sum(item['quantity'] for item in cart.values())

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({
            'success': True,
            'cart_count': cart_count,
            'message': 'Товар добавлен в корзину'
        })

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