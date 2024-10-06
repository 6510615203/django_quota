from django.urls import path
from login import views

urlpatterns = [
    path("",views.index, name="index"),
    path("quota/",views.quota, name="quota"),
    path("search",views.search, name="search"),
    path("result",views.result, name="result")
]