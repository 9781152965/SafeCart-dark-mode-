from django.urls import path
from . import views
from .views import *


app_name = 'shop'
urlpatterns = [
   
    path("", views.index, name="ShopHome"),
    path("about/", views.about, name="AboutUs"),
    path("home/", home.as_view(), name="home"),
    path("allproducts/", AllProductView.as_view(), name="allproducts"),
    path("add-to-cart<int:pro_id>/", AddToCartView.as_view(), name="addtocart"),

    path("contact/", views.contact, name="ContactUs"),
    path("tracker/", views.tracker, name="TrackingStatus"),
    path("search/", views.search, name="Search"),
    path("products/<int:myid>", views.productView, name="ProductView"),
    path("checkout/", views.checkout, name="Checkout"),
]
