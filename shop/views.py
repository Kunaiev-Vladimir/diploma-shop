from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Product, Category

# Create your views here.

#def product_list(request):
    #products = Product.objects.filter(is_available=True)
    #return render(request, 'shop/product_list.html', {'products': products})
    
from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from .models import Product, Category


def product_list(request):
    products = Product.objects.filter(is_available=True)
    categories = Category.objects.filter(is_active=True)

    q = request.GET.get('q')
    category_slug = request.GET.get('category')

    if q:
        products = products.filter(
            Q(name__icontains=q) |
            Q(description__icontains=q) |
            Q(category__name__icontains=q)
        )

    if category_slug:
        products = products.filter(category__slug=category_slug)

    context = {
        'products': products,
        'categories': categories,
        'q': q,
        'category_slug': category_slug,
    }

    return render(request, 'shop/product_list.html', context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_available=True)
    return render(request, 'shop/product_detail.html', {'product': product})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_available=True)
    return render(request, 'shop/product_detail.html', {'product': product})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_available=True)
    return render(request, 'shop/product_detail.html', {'product': product})