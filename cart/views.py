from django.shortcuts import render, redirect, get_object_or_404
from shop.models import Product
from django.http import JsonResponse
# from .services import get_cart_items
# from .services import get_cart_items, add_product_to_cart
from .services import get_cart_items, add_product_to_cart, update_product_quantity

# Create your views here.


# def cart_detail(request):
#     cart = request.session.get('cart', {})
#     cart_items = []
#     total_price = 0

#     for product_id, item in cart.items():
#         product = Product.objects.get(id=product_id)

#         if isinstance(item, dict):
#             quantity = item.get('quantity', 1)
#         else:
#             quantity = item

#         item_total = product.price * quantity
#         total_price += item_total

#         cart_items.append({
#             'product': product,
#             'quantity': quantity,
#             'total_price': item_total,
#         })

#     return render(request, 'cart/cart_detail.html', {
#         'cart_items': cart_items,
#         'total_price': total_price,
#     })


# def cart_detail(request):
#     cart = request.session.get('cart', {})
#     cart_items = []
#     total_price = 0

#     product_ids = cart.keys()
#     products = Product.objects.filter(id__in=product_ids)
#     products_dict = {str(product.id): product for product in products}

#     for product_id, item in cart.items():
#         product = products_dict.get(str(product_id))

#         if not product:
#             continue

#         if isinstance(item, dict):
#             quantity = item.get('quantity', 1)
#         else:
#             quantity = item

#         item_total = product.price * quantity
#         total_price += item_total

#         cart_items.append({
#             'product': product,
#             'quantity': quantity,
#             'total_price': item_total,
#         })

#     return render(request, 'cart/cart_detail.html', {
#         'cart_items': cart_items,
#         'total_price': total_price,
#     })


def cart_detail(request):
    """Display shopping cart."""
    cart = request.session.get('cart', {})
    cart_items, total_price = get_cart_items(cart)

    return render(request, 'cart/cart_detail.html', {
        'cart_items': cart_items,
        'total_price': total_price,
    })


# def cart_add(request, product_id):
    # cart = request.session.get('cart', {})

    # if str(product_id) in cart:
    # cart[str(product_id)] += 1
    # else:
    # cart[str(product_id)] = 1

    # request.session['cart'] = cart
    # request.session.modified = True

    # return redirect(request.META.get('HTTP_REFERER', 'shop:product_list'))


def cart_add(request, product_id):
    """Add product to cart."""
    product = get_object_or_404(Product, id=product_id)

    cart = request.session.get('cart', {})

    # product_id_str = str(product.id)

    # if product_id_str in cart:
    #     cart[product_id_str]['quantity'] += 1
    # else:
    #     cart[product_id_str] = {
    #         'quantity': 1,
    #         'price': str(product.price),
    #     }

    cart = add_product_to_cart(cart, product)

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
    """Remove product from cart."""
    cart = request.session.get('cart', {})

    if str(product_id) in cart:
        del cart[str(product_id)]

    request.session['cart'] = cart

    return redirect('cart:cart_detail')

# def update_cart(request, product_id):
    # if request.method == 'POST':
    # quantity = int(request.POST.get('quantity', 1))
    # cart = request.session.get('cart', {})

    # if str(product_id) in cart:
    # cart[str(product_id)] = quantity

    # request.session['cart'] = cart

    # return redirect('cart:cart_detail')


def update_cart(request, product_id):
    """Update product quantity in cart."""
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        cart = request.session.get('cart', {})

        # product_id_str = str(product_id)

        # product = get_object_or_404(Product, id=product_id)

        # if quantity > 0:
        #     cart[product_id_str] = {
        #         'quantity': quantity,
        #         'price': str(product.price),
        #     }
        # else:
        #     cart.pop(product_id_str, None)

        product = get_object_or_404(Product, id=product_id)
        cart = update_product_quantity(cart, product, quantity)

        request.session['cart'] = cart
        request.session.modified = True

    return redirect('cart:cart_detail')
