''' authentication, or allowing users to log in and out of a website. 
Fortunately, Django makes this very easy for us 

Now, we’ll add three functions:'''

from flights import views
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User
from django import forms
from .forms import UserRegistrationForm,UserBookingForm
from flights.models import *


# Create your views here.
def index(request):
    # If no user is signed in, return to login page:
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login_link"))
    return render(request, "users/user.html")

def login_view(request):
    if request.method == "POST":
    	  # Accessing username and password from form data
        username = request.POST["username"]
        password = request.POST["password"]

         # Check if username and password are correct, returning User object if so
        user = authenticate(request, username=username, password=password)

        # If user object is returned, log in and route to index page:
        if user is not None:
            login(request, user)
            return render(request, "users/login.html", {
                "message": f"Welcome {username.upper()} you are logged in."
            })

            # Otherwise, return login page again with new context
        else:
            return render(request, "users/login.html", {
                "message": "Invalid credentials."
            })
    else:
        return render(request, "users/login.html")

#To allow the user to log out, we’ll write the logout_view function 
#so that it uses Django’s built-in logout function

def logout_view(request):
    logout(request)
    return render(request, "users/login.html", {
        "message": "Logged out."
    })

# creating a register form for new users to register their details 
#first before been redirected to login page for login

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            email =  userObj['email']
            password =  userObj['password']
            first_name = userObj['first_name']
            last_name = userObj['last_name']
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                User.objects.create_user(username, email, password, first_name= first_name, last_name= last_name)
                
                #from the site registration form, i coolected the user first name and
                #last name and add automaticallt to the passesnger model
                passenger = Passenger(first=first_name, last=last_name)
                passenger.save()

                user = authenticate(username = username, password = password)
                login(request, user)
                return render(request, "users/login.html")
            else:
                return render(request, "users/register.html", {
                "message": "'Looks like a username with that email or password already exists'", 'form' : form})
                
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form' : form})


def booking_form(request):
    if request.method == 'POST':
        form = UserBookingForm(request.POST) 
        if form.is_valid():
            userObj = form.cleaned_data
            first_name = userObj['first_name']
            last_name = userObj['last_name']
            gender = userObj['gender']
            origin = userObj['origin']
            destination = userObj['destination']
            email = userObj['email']
            phone = userObj['phone']
            
        
            passenger_data = Passenger(first=first_name, last=last_name)
            passenger_data.save()
            flight_data = Flight(origin=origin, destination=destination) 
            flight_data.save()
            book_record = Book_record(first=first_name, last=last_name,gender = gender, origin=origin, destination=destination, email=email,phone=phone )
            book_record.save()
               
            return HttpResponseRedirect(reverse('flight_index'))
        else:
            return render(request, "users/booking.html", {
            "message": "'Looks like you didnt register correctly", 'form' : form})
                
    else:
        form = UserBookingForm()
    return render(request, 'users/booking.html', {'form' : form})



