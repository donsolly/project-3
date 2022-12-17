from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import *
from .forms import *

# Create your views here.
# def index(request):
#     return HttpResponse("Project 3: TODO")

def index(request):
   if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message": None})
   context = {

      "Pizza": Menu.objects.all(),
      "Topping": Toppings.objects.all(),
      "user_cart": Cart.objects.filter(user=request.user)

   }
   return render(request, "orders/index.html", context)


def login_user(request):
   if request.method == 'POST':
      username = request.POST['username']
      password = request.POST['password']
      user = authenticate(request, username=username, password=password)
      if user is not None:
         login(request, user)
         return HttpResponseRedirect(reverse("index"))
      else:
         return render(request, "orders/login.html", {"message": "Invalid credentials."})
   else:
      return render(request, "orders/login.html", {"message": "Please Login."})

def signup_user(request):
   if request.method == 'POST':
      form = SignUpForm(request.POST)
      if form.is_valid():
         form.save()
         username = form.cleaned_data.get('username')
         raw_password = form.cleaned_data.get('password1')
         user = authenticate(username=username, password=raw_password)
         login(request, user)
         return redirect('index')
   else:
      form = SignUpForm()
   return render(request, 'orders/register.html', {'form': form})

def logout_user(request):
   logout(request)
   return render(request, "orders/login.html", {"message": "Logged out."})


def cart(request):
   template = "orders/index.html"
   if request.method == 'POST':
      category = request.POST['category-cart']
      main = request.POST["main-cart"]
      size = request.POST["size-cart"]
      price = request.POST["price-cart"]
      user = request.user
      user_cart = Cart(category=category,main=main,size=size,price=price,user=user)
      user_cart.save()
      return redirect('index')
   else:
      return render(request, "index", {"message": "Fill an order"})

def cart_1(request):
   template = "orders/index.html"
   if request.method == 'POST':
      category = request.POST['category-cart']
      topping = request.POST["topping-cart"]
      main = request.POST["main-cart"]
      size = request.POST["size-cart"]
      price = request.POST["price-cart"]
      user = request.user
      user_cart = Cart(category=category,main=main,size=size,price=price,user=user,topping=topping)
      user_cart.save()
      return redirect('index')
   else:
      return render(request, "index", {"message": "Fill an order"})

def cart_2(request):
   template = "orders/index.html"
   if request.method == 'POST':
      category = request.POST['category-cart']
      topping = request.POST["topping-cart"]
      topping1 = request.POST["topping-cart1"]
      main = request.POST["main-cart"]
      size = request.POST["size-cart"]
      price = request.POST["price-cart"]
      user = request.user
      user_cart = Cart(category=category,main=main,size=size,price=price,user=user,topping1=topping1,topping=topping)
      user_cart.save()
      return redirect('index')
   else:
      return render(request, "index", {"message": "Fill an order"})

def cart_3(request):
   template = "orders/index.html"
   if request.method == 'POST':
      category = request.POST['category-cart']
      main = request.POST["main-cart"]
      size = request.POST["size-cart"]
      price = request.POST["price-cart"]
      topping = request.POST["topping-cart"]
      topping1 = request.POST["topping-cart1"]
      topping2 = request.POST["topping-cart2"]
      user = request.user
      user_cart = Cart(category=category,main=main,size=size,price=price,user=user,topping=topping,topping1=topping1,topping2=topping2,)
      user_cart.save()
      return redirect('index')
   else:
      return render(request, "index", {"message": "Fill an order"})


def delete_cart(request):
   template = "orders/index.html"
   if request.method == 'POST':
      cart_id = request.POST['id-cart']
      Cart.objects.filter(id=cart_id).delete()
      return redirect('checkout')
   else:
      return render(request, "index", {"message": "Fill an order"})


def checkout(request):
   if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message": None})
   context = {

      "user_cart": Cart.objects.filter(user=request.user)

   }
   return render(request, "orders/cart.html", context)


def purchase(request):
   template = "orders/cart.html"
   if request.method == 'POST':
      user = request.user
      total = request.POST['total_order']
      products = request.POST['products']
      description = request.POST['description']
      quantity = request.POST['quantity']
      subtotal = request.POST['subtotal']
      price = request.POST['price']
      new_order = Orders(user=user,total=total,products=products,description=description,quantity=quantity,subtotal=subtotal,price=price)
      new_order.save()
      Cart.objects.filter(user=user).delete()

      return render(request, "orders/complete.html")
   else:
      return render(request, "index", {"message": "Fill an order"})

def history(request):
   if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message": None})
   context = {

      "history": Orders.objects.filter(user=request.user)

   }
   return render(request, "orders/history.html", context)




#where we put all 