from django.shortcuts import render
from django.views import View
from .models import Customer, Product, Cart, OrderPlaced

# class of product 
class ProductView(View):
    def get(self, request):
        mobiles = Product.objects.filter(category='M')
        laptops = Product.objects.filter(category='L')
        return render(request, 'home.html', {'mobiles':mobiles, 'laptops':laptops})

class ProductDetailView(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return render(request, 'productdetail.html', {'product':product})

def add_to_cart(request):
    return render(request, "addtocart.html")


def buy_now(request):
    return render(request, "buynow.html")


def profile(request):
    return render(request, "profile.html")


def address(request):
    return render(request, "address.html")


def orders(request):
    return render(request, "orders.html")


def change_password(request):
    return render(request, "changepassword.html")


def mobile(request):
    return render(request, "mobile.html")


def login(request):
    return render(request, "login.html")


def customerregistration(request):
    return render(request, "customerregistration.html")


def checkout(request):
    return render(request, "checkout.html")