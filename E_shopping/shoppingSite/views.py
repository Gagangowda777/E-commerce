from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'shoppingSite/index.html')

def category(request):
    return render(request, "shoppingSite/category.html")

def cart(request):
    return render(request, "shoppingSite/cart.html")

def user(request):
    return render(request, "shoppingSite/user.html")

def login(request):
    return render(request, "shoppingSite/login.html")