from django.shortcuts import render, redirect


# Create your views here.


def home(request):
    """A view that displays the home page"""
    return render(request, "home.html")


def index(request):
    """A view that displays the index page"""
    return render(request, "index.html")


def contact(request):
    """A view that displays the contact page"""
    return render(request, "contact.html")
