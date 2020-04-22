from django.shortcuts import render
from .models import Product

# Create your views here.


def all_products(request):
    products = Product.objects.all().order_by('category')
    return render(request, "products.html", {"products": products})


def baby(request):
    products = Product.objects.all()
    return render(request, "baby.html", {"products": products})


def christening(request):
    products = Product.objects.all()
    return render(request, "christening.html", {"products": products})


def communions(request):
    products = Product.objects.all()
    return render(request, "communions.html", {"products": products})


def engagement(request):
    products = Product.objects.all()
    return render(request, "engagement.html", {"products": products})


def family(request):
    products = Product.objects.all()
    return render(request, "family.html", {"products": products})


def fathersday(request):
    products = Product.objects.all()
    return render(request, "fathersday.html", {"products": products})


def fingerprint(request):
    products = Product.objects.all()
    return render(request, "fingerprint.html", {"products": products})


def mothersday(request):
    products = Product.objects.all()
    return render(request, "mothersday.html", {"products": products})


def teacher(request):
    products = Product.objects.all()
    return render(request, "teacher.html", {"products": products})


def wedding(request):
    products = Product.objects.all()
    return render(request, "wedding.html", {"products": products})
