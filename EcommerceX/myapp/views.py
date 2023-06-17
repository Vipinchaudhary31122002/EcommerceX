from django.shortcuts import render
from django.views import View
from .models import Customer, Product, Cart, OrderPlaced
from .forms import CustomerRegistrationForm
from django.contrib import messages

# view for home page
class ProductView(View):
    def get(self, request):
        mobiles = Product.objects.filter(category='M')
        laptops = Product.objects.filter(category='L')
        return render(request, 'home.html', {'mobiles':mobiles, 'laptops':laptops})

# view for product detail page
class ProductDetailView(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return render(request, 'productdetail.html', {'product':product})

# view for customer registration page
class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'customerregistration.html', {'form':form})

    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulations! Registration Successfull')
            form.save()
        return render(request, 'customerregistration.html', {'form':form})

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

def login(request):
    return render(request, "login.html")


def checkout(request):
    return render(request, "checkout.html")