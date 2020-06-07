from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from orders.models  import pizza
import math
# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request,"login.html",{"message":None})
    print(pizza.objects.all().values())
    pizza_entries = list(pizza.objects.all()) #force list to split half
    half = int(math.ceil(len(pizza_entries)/2))
    pizza1 = pizza_entries[:half]
    pizza2 = pizza_entries[half:]
    context = {
        "user" : request.user,
        "pizza1":  pizza1,
        "pizza2":  pizza2
    }
    return render(request, 'user.html',context)

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
