from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # url of home page
    path("", views.ProductView.as_view(), name="home"),
    # url of product detail-page
    path("product-detail/<int:pk>", views.ProductDetailView.as_view(), name="product-detail"),
    # url of customerregistration page 
    path("registration/", views.CustomerRegistrationView.as_view(), name="customerregistration"),
    
    path("cart/", views.add_to_cart, name="add-to-cart"),
    path("buy/", views.buy_now, name="buy-now"),
    path("profile/", views.profile, name="profile"),
    path("address/", views.address, name="address"),
    path("orders/", views.orders, name="orders"),
    path("changepassword/", views.change_password, name="changepassword"),
    path("login/", views.login, name="login"),
    path("checkout/", views.checkout, name="checkout"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)