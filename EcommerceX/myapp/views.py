from django.shortcuts import render

def home(request):
 return render(request, 'home.html')

def product_detail(request):
 return render(request, 'productdetail.html')

def add_to_cart(request):
 return render(request, 'addtocart.html')

def buy_now(request):
 return render(request, 'buynow.html')

def profile(request):
 return render(request, 'profile.html')

def address(request):
 return render(request, 'address.html')

def orders(request):
 return render(request, 'orders.html')

def change_password(request):
 return render(request, 'changepassword.html')

def mobile(request):
 return render(request, 'mobile.html')

def login(request):
 return render(request, 'login.html')

def customerregistration(request):
 return render(request, 'customerregistration.html')

def checkout(request):
 return render(request, 'checkout.html')