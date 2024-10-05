from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,"index.html")

def quota(request):
    return render(request,"quota.html")

def search(request):
    return render(request,"search.html")

def result(request):
    return render(request,"result.html")