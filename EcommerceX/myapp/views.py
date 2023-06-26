from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views import View
from .models import Customer, Product, Cart, OrderPlaced
from .forms import CustomerProfileForm, CustomerRegistrationForm
from django.contrib import messages
from django.db.models import Q

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

# view for address page
def address(request):
    add = Customer.objects.filter(user=request.user)
    return render(request, "address.html", {'add':add, 'active':'btn-primary'})

# view for add to cart
def add_to_cart(request):
    user=request.user
    product_id=request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    Cart(user=user, product=product).save()
    return redirect('/cart')

# view for showing the cart product
def show_cart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)
        # print(cart)
        amount = 0.0
        shipping_amount = 100
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == user]
        # print(cart_product)
        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity*p.product.discounted_price)
                amount+=tempamount
                totalamount = amount + shipping_amount
            return render(request, "addtocart.html", {'carts':cart, 'totalamount': totalamount, 'amount':amount})
        else:
            return render(request, 'emptycart.html')

# view for plus button 
def plus_cart(request):
    if request.method== 'GET':
        prod_id = request.GET['prod_id']
        print('prod_id')
        c = Cart.objects.get(Q(product = prod_id) & Q(user=request.user))
        c.quantity+=1
        c.save()
        amount = 0.0
        shipping_amount = 100.00
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity*p.product.discounted_price)
            amount+=tempamount
            totalamount = amount
        data = {
            'quantity': c.quantity,
            'amount':amount,
            'totalamount': totalamount  + shipping_amount
        }
        return JsonResponse(data)

# view for minus button
def minus_cart(request):
    if request.method== 'GET':
        prod_id = request.GET['prod_id']
        print('prod_id')
        c = Cart.objects.get(Q(product = prod_id) & Q(user=request.user))
        c.quantity-=1
        c.save()
        amount = 0.0
        shipping_amount = 100.00
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity*p.product.discounted_price)
            amount +=tempamount
            totalamount = amount
        data = {
            'amount':amount,
            'totalamount': totalamount + shipping_amount
        }
        return JsonResponse(data)
    
def remove_cart(request):
    if request.method== 'GET':
        prod_id = request.GET['prod_id']
        print('prod_id')
        c = Cart.objects.get(Q(product = prod_id) & Q(user=request.user))
        c.delete()
        amount = 0.0
        shipping_amount = 100.00
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity*p.product.discounted_price)
            amount +=tempamount
            totalamount = amount
        data = {
            'amount':amount,
            'totalamount': totalamount + shipping_amount
        }
        return JsonResponse(data)

# view for checkout page
def checkout(request):
    user = request.user
    add = Customer.objects.filter(user=user)
    cart_items = Cart.objects.filter(user=user)
    amount = 0.0
    shipping_amount = 100.0
    total_amount = 0.0
    cart_product = [p for p in Cart.objects.all() if p.user == request.user]
    if cart_product:
        for p in cart_product:
            tempamount = (p.quantity*p.product.discounted_price)
            amount+=tempamount
            totalamount = amount
        totalamount = amount + shipping_amount
    return render(request, "checkout.html", {'add':add, 'totalamount':totalamount, 'cartitems':cart_items, 'totalamount':totalamount})







def buy_now(request):
    return render(request, "buynow.html")

def orders(request):
    return render(request, "orders.html")

def change_password(request):
    return render(request, "changepassword.html")


