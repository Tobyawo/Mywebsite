from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
path('', views.index, name="mysite_index"),
path('about', views.about, name="about"),
path('contact', views.contact, name="contact"),

]