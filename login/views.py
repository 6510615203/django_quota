from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
    if request.method =="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect("quota")
        else:
            return render(request, "index.html", {
                "message": "Invalid credentials."
            })
        
    return render(request, "index.html")


def quota(request):
    return render(request,"quota.html")

def search(request):
    return HttpResponse("Search")

def result(request):
    return HttpResponse("Result")