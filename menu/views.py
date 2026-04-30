from django.shortcuts import render
from django.db.models import Prefetch
from shop.models import Category, Product


def get_sorted_products(request):
    sort = request.GET.get('sort')

    products = Product.objects.filter(is_available=True)

    if sort == 'cheap':
        products = products.order_by('price')
    elif sort == 'expensive':
        products = products.order_by('-price')
    elif sort == 'new':
        products = products.order_by('-created_at')
    else:
        products = products.order_by('name')

    return products, sort


def menu_list(request):
    products, sort = get_sorted_products(request)

    categories = Category.objects.filter(is_active=True).prefetch_related(
        Prefetch('products', queryset=products)
    )

    return render(request, 'menu/menu_list.html', {
        'categories': categories,
        'sort': sort,
    })


def menu_by_category(request, slug):
    products, sort = get_sorted_products(request)

    products = products.filter(category__slug=slug)

    categories = Category.objects.filter(is_active=True).prefetch_related(
        Prefetch('products', queryset=products)
    )

    return render(request, 'menu/menu_list.html', {
        'categories': categories,
        'sort': sort,
        'active_slug': slug,
    })