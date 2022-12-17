from django.urls import path

from . import views

urlpatterns = [
   path("", views.index, name="index"),
   path("login", views.login_user, name="login"),
   path("logout", views.logout_user, name="logout"),
   path("signup", views.signup_user, name="signup"),
   path("cart", views.cart, name="cart"),
   path("cart_1", views.cart_1, name="cart_1"),
   path("cart_2", views.cart_2, name="cart_2"),
   path("cart_3", views.cart_3, name="cart_3"),
   path("delete_cart", views.delete_cart, name="delete_cart"),
   path("checkout", views.checkout, name="checkout"),
   path("purchase", views.purchase, name="purchase"),
   path("history", views.history, name="history"),
]
