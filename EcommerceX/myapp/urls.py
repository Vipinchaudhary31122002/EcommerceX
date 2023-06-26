from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import CustomerAuthenticationForm, MyPasswordChangeForm

urlpatterns = [
    # url of home page
    path("", views.ProductView.as_view(), name="home"),
    # url of product detail-page
    path("product-detail/<int:pk>", views.ProductDetailView.as_view(), name="product-detail"),
    # url of customerregistration page 
    path("registration/", views.CustomerRegistrationView.as_view(), name="customerregistration"),
    # url of login page
    path("accounts/login/", auth_views.LoginView.as_view(template_name='login.html', authentication_form=CustomerAuthenticationForm), 
    name="login"),
    #  url for logout
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    # url for password change 
    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='changepassword.html', form_class=MyPasswordChangeForm, success_url='/passwordchangedone/'), name='passwordchange'),
    #  url for password change done
    path('passwordchangedone/', views.ProductView.as_view(), name='passwordchangedone'),
    # url of profile page
    path("profile/", views.ProfileView.as_view(), name="profile"),
    # url of add to cart
    path("add-to-cart/", views.add_to_cart, name="add-to-cart"),
    # url of show cart
    path("cart/", views.show_cart, name="showcart"),
    # plus cart
    path("pluscart/", views.plus_cart),
    # minus cart
    path("minuscart/", views.minus_cart),
    # remove cart
    path("removecart/", views.remove_cart,),
    # url for address page
    path("address/", views.address, name="address"),
    # url for checkout page
    path("checkout/", views.checkout, name="checkout"),





    path("buy/", views.buy_now, name="buy-now"),    
    path("orders/", views.orders, name="orders"),
    path("changepassword/", views.change_password, name="changepassword"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)