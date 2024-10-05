from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,"index.html")

def quota(request):
    return render(request,"quota.html")

def search(request):
    return HttpResponse("Search")

def result(request):
    return HttpResponse("Result")