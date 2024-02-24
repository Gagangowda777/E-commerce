from django.urls import path 

from . import views

app_name = "shopping"
urlpatterns = [
    path("", views.index, name="index"),
    path("/category", views.category, name="category"),
    path("/cart", views.cart, name="cart"),
    path("/user", views.user, name="user"),
    path("/login", views.login, name="login")
]
