from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from login.models import Student, Subject, Enrollment
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

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
    query = request.POST.get("q")
    if query:
        subject_list = subject_list.filter(code__icontains=query) | subject_list.filter(name__icontains=query)

    if request.method == "POST":
        code = request.POST.get("code")
        if code :
            subject = get_object_or_404(Subject, code=code)
            student = get_object_or_404(Student, user=request.user)
            enrollment = Enrollment(student=student, subject=subject)
            subject.seats = subject.seats - 1
            subject.status = "REGISTERED"
            subject.save()
            enrollment.save()

    return render(request,"quota.html",{"subject_list":subject_list})

def search(request):
    subject_list = Subject.objects.all()
    query = request.POST.get("q")
    if query:
        subject_list = subject_list.filter(code__icontains=query) | subject_list.filter(name__icontains=query)
    return render(request,"search.html",{"subject_list":subject_list})

def result(request):
    return render(request,"result.html")