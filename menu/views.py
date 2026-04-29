from django.shortcuts import render
from shop.models import Category


def menu_list(request):
    categories = Category.objects.filter(is_active=True).prefetch_related('products')

    return render(request, 'menu/menu_list.html', {
        'categories': categories
    })