from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Product

# Create your views here.

#def product_list(request):
    #products = Product.objects.filter(is_available=True)
    #return render(request, 'shop/product_list.html', {'products': products})
    
def product_list(request):
    query = request.GET.get('q', '')

    products = Product.objects.filter(is_available=True)

    if query:
        products = products.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(category__name__icontains=query)
        )

    return render(request, 'shop/product_list.html', {
        'products': products,
        'query': query,
    })


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_available=True)
    return render(request, 'shop/product_detail.html', {'product': product})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_available=True)
    return render(request, 'shop/product_detail.html', {'product': product})