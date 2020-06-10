from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.db.models import Sum
from django.contrib.auth import authenticate, login, logout
from orders.models  import pizza,toppings,order,sub,sub_addition
from django.db import models
import math
# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request,"login.html",{"message":None})

    pizza_entries = list(pizza.objects.all()) #force list to split half
    half = int(math.ceil(len(pizza_entries)/2))
    pizza1 = pizza_entries[:half]
    pizza2 = pizza_entries[half:]

    sub_entries = list(sub.objects.all()) #force list to split half
    half = int(math.ceil(len(sub_entries)/2))
    sub1 = sub_entries[:half]
    sub2 = sub_entries[half:]


    toppings_entries = toppings.objects.all()

    context = {
        "user" : request.user,
        "pizza1":  pizza1,
        "pizza2":  pizza2,
        "sub1":  sub1,
        "sub2":  sub2,
        "toppings": toppings_entries
    }
    return render(request, 'user.html',context)

#cart views
def cart_view(request):
    order_entry = order.objects.filter(Name = request.user)
    total = order.objects.filter(Name = request.user).aggregate(Sum('Price',
                                    output_field = models.DecimalField(max_digits=4, decimal_places=2)))
    context = {
        "user" : request.user,
        "orders": order_entry,
        "total_price":total['Price__sum']
    }

    return render(request, 'cart.html',context)

#login
def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "login.html",{"message":"Invalid Credentials"})


#logout
def logout_view(request):
    logout(request)
    return render(request, "login.html", {"message":"Logged out."})

#delete from cart
def delete_from_cart(request):
    id_to_be_deleted = dict(request.POST)['order_id'][0]
    entry = order.objects.get(id = id_to_be_deleted)
    entry.delete()
    return HttpResponse(status=200)

#submit_order
def submitorderpizza(request):
    data = dict(request.POST)
    data_keys = data.keys()
    type = data['Type'][0]
    size = data['Size'][0]
    topping1 = None
    topping2 = None
    topping3 = None
    if 'defaultIngredient' in data_keys:
        details = data['defaultIngredient'][0]
    else:
        if 'Topping 1' in data_keys:
            details = '1 Topping'
            topping1 = toppings.objects.get(Type = data['Topping 1'][0])
        if 'Topping 2' in data_keys:
            details = '2 Toppings'
            topping2 = toppings.objects.get(Type = data['Topping 2'][0])
        if 'Topping 3' in data_keys:
            details = '3 Toppings'
            topping3 = toppings.objects.get(Type = data['Topping 3'][0])

    pizza_entry = pizza.objects.get(Type = type, Size = size,
                                    Details = details)

    new_order = order(Name = request.user, content_object = pizza_entry,
                        Topping_1 = topping1, Topping_2 = topping2, Topping_3 = topping3,
                        Sub_1=None,Sub_2 = None,Sub_3= None,Sub_4=None,Price = pizza_entry.Price)

    new_order.save()

    # order_entry = order.objects.all()
    # for i in order_entry:
    #     print(i.Name, i.content_object.Type, i.content_object.Size, i.content_object.Details ,i.Topping_1, i.content_object.Price)
    # print(order_entry)
    return HttpResponseRedirect(reverse("index"))

#submit sub order
def submitordersub(request):
    data = dict(request.POST)
    data_keys = data.keys()
    type = data['Type'][0]
    size = data['Size'][0]
    sub1 = None
    sub2 = None
    sub3 = None
    sub4 = None
    sub_entry = sub.objects.get(Type = type, Size = size)
    price = sub_entry.Price
    if 'extraCheese' in data_keys:
        sub1 = sub_addition.objects.get(Type = data['extraCheese'][0]) #"Extra Cheese"
        price += sub1.AdditionalPrice
    if 'steakCheese' in data_keys:
        sub1 = sub_addition.objects.get(Type = data['steakCheese'][0], Size = size)
        price += sub1.AdditionalPrice
    if 'steakMushrooms' in data_keys:
        sub2 = sub_addition.objects.get(Type = data['steakMushrooms'][0])
        price += sub2.AdditionalPrice
    if 'steakGreenPeppers' in data_keys:
        sub3 = sub_addition.objects.get(Type = data['steakGreenPeppers'][0])
        price += sub3.AdditionalPrice
    if 'steakOnions' in data_keys:
        sub4 = sub_addition.objects.get(Type = data['steakOnions'][0])
        price += sub4.AdditionalPrice


    new_order = order(Name = request.user, content_object = sub_entry,
                        Topping_1 = None, Topping_2 = None, Topping_3 = None,
                        Sub_1=sub1,Sub_2 = sub2,Sub_3= sub3,Sub_4=sub4, Price = price)

    new_order.save()

    # order_entry = order.objects.all()
    # for i in order_entry:
    #     print(i.Name, i.content_object.Type, i.content_object.Size ,i.Topping_1, i.Sub_1,
    #             i.Sub_2.Type,i.Sub_3.Type,i.content_object.Price)

    return HttpResponseRedirect(reverse("index"))
