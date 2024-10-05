from django.urls import path
from login import views

urlpatterns = [
    path("",views.index),
    path("quota",views.quota),
    path("search",views.search),
    path("result",views.result)
]