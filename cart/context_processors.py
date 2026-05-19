

def cart_count(request):
    cart = request.session.get('cart', {})

    total_count = 0

    for item in cart.values():
        if isinstance(item, dict):
            total_count += item.get('quantity', 0)
        else:
            total_count += item

    return {
        'cart_count': total_count
    }
