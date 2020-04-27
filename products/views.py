from django.shortcuts import render
from .models import Product

# Create your views here.


def all_products(request):
    products = Product.objects.all().order_by('category')
    return render(request, "products.html", {"products": products})


def category_view(request, category):
    products = Product.objects.filter(category__iexact=category).all()
    return render(request, "product_category.html", {"products": products, 'title': category.lower().title() + ' Prints'})


def gallery(request):
    return render(request, "gallery.html")
