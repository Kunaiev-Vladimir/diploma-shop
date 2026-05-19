from shop.models import Product


def get_cart_items(cart):
    cart_items = []
    total_price = 0

    product_ids = cart.keys()
    products = Product.objects.filter(id__in=product_ids)
    products_dict = {str(product.id): product for product in products}

    for product_id, item in cart.items():
        product = products_dict.get(str(product_id))

        if not product:
            continue

        if isinstance(item, dict):
            quantity = item.get('quantity', 1)
        else:
            quantity = item

        item_total = product.price * quantity
        total_price += item_total

        cart_items.append({
            'product': product,
            'quantity': quantity,
            'total_price': item_total,
        })

    return cart_items, total_price
