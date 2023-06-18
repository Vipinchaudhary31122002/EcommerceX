from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import CustomerAuthenticationForm

urlpatterns = [
    # url of home page
    path("", views.ProductView.as_view(), name="home"),
    # url of product detail-page
    path("product-detail/<int:pk>", views.ProductDetailView.as_view(), name="product-detail"),
    # url of customerregistration page 
    path("registration/", views.CustomerRegistrationView.as_view(), name="customerregistration"),
    # url of login page
    path("accounts/login/", auth_views.LoginView.as_view(template_name='login.html', authentication_form=CustomerAuthenticationForm), name="login"),
    # url of profile page
    path("profile/", views.profile, name="profile"),
    path("cart/", views.add_to_cart, name="add-to-cart"),
    path("buy/", views.buy_now, name="buy-now"),    
    path("address/", views.address, name="address"),
    path("orders/", views.orders, name="orders"),
    path("changepassword/", views.change_password, name="changepassword"),
    path("checkout/", views.checkout, name="checkout"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)