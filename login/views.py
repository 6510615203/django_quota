from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from login.models import Student, Subject
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
    if request.method =="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if username == "admin":
                return HttpResponseRedirect("admin")
            return HttpResponseRedirect("quota")
        else:
            return render(request, "index.html", {
                "message": "Invalid credentials."
            })
        
    return render(request, "index.html")


def quota(request):
    subject_list = Subject.objects.all()
    return render(request,"quota.html",{"subject_list":subject_list})

def search(request):
    subject_list = Subject.objects.all()
    query = request.POST.get("q")
    if query:
        subject_list = subject_list.filter(code__icontains=query) | subject_list.filter(name__icontains=query)
    return render(request,"search.html",{"subject_list":subject_list})

def result(request):
    return render(request,"result.html")