from django.contrib import admin
from django.urls import path
from shop import views

urlpatterns = [
    path("", views.index, name='shop'), # koi bhi khali path lekr aata hai to usko views ke index function pr bhej do, aur is path ka naam rakh do home
    path("about", views.about, name='about'),
]
