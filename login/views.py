from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,"index.html")

def about(request):
    return HttpResponse("Hello mommy jaemin")

def form(request):
    return HttpResponse("Hello mommy renjun")