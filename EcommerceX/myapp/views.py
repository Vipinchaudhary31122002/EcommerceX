from django.shortcuts import render
from django.views import View
from .models import Customer, Product, Cart, OrderPlaced
from .forms import CustomerProfileForm, CustomerRegistrationForm
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
            messages.success(request, 'Congratulations! Registration Successfull. Please login')
            form.save()
        return render(request, 'customerregistration.html', {'form':form})
    
# view for profile page
class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        return render(request, 'profile.html', {'form':form, 'active':'btn-primary'})

    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            usr = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            reg = Customer(user=usr, name=name, locality=locality, city=city, state=state, zipcode=zipcode)
            reg.save()
            messages.success(request, 'Congratulations! profile updated Successfully')
        return render(request, 'profile.html', {'form':form, 'active':'btn-primary'})


def add_to_cart(request):
    return render(request, "addtocart.html")

def buy_now(request):
    return render(request, "buynow.html")


def address(request):
    return render(request, "address.html")


def orders(request):
    return render(request, "orders.html")


def change_password(request):
    return render(request, "changepassword.html")


def checkout(request):
    return render(request, "checkout.html")

