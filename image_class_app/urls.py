from django.urls import path
from . import views


'''let’s add a few more pages to our site. We’ll begin by adding the 
ability to click on a flight to get more information about it. and book a flight
To do this, let’s create a URL path that includes the id of a flight:'''

urlpatterns = [
path('', views.index, name="image_index"),
#path('result/', views.result, name="image_result"),
]