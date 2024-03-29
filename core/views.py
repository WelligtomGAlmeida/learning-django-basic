from django.shortcuts import render
from .models import Product


def index(request):
    products = Product.objects.all()

    context = {
        'course': 'Web Programming with Django Framework',
        'products': products
    }

    return render(request, 'index.html', context)


def contact(request):
    return render(request, 'contact.html')


def product(request, id):
    prod = Product.objects.get(id=id)
    context = {
        'product': prod
    }
    return render(request, 'product.html', context)