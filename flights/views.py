from django.shortcuts import render

# Create your views here.
from django import forms
from django.http import HttpResponseBadRequest, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse

from flights.models import *
from users.forms import UserBookingForm

# Create your views here.

def index_user(request): 
    return render(request, "flights/index.html")

def index_submit(request): 
    records = Book_record.objects.get(id=1)
    return render(request, "flights/index.html", {
        "records": records 
    })

'''Now, let’s add a few more pages to our site. We’ll begin by adding the 
ability to click on a flight to get more information about it. 
To do this, let’s create a URL path that includes the id of a flight:
Then, in views.py we will create a flight function that takes in a 
flight id and renders a new html page: '''

'''
Now, let’s work on giving visitors to our site the ability to book a flight. 
We’ll do this by adding a booking route in urls.py: '''

'''
def book(request, flight_id):

    # For a post request, add a new flight
    if request.method == "POST":

        # Accessing the flight
        flight = Flight.objects.get(pk=flight_id)

        # Finding the passenger id from the submitted form data
        passenger_id = int(request.POST["passenger"])

        # Finding the passenger based on the id
        passenger = Passenger.objects.get(pk=passenger_id)

        # Add passenger to the flight
        passenger.flights.add(flight)

        # Redirect user to flight page
        return HttpResponseRedirect(reverse("flight", args=(flight.id,)))

'''#priority = forms.IntegerField(label="Priority", min_value=1,max_value=10)

def index(request):
    #storing tasks inside of the user's sessions instead of global variable
     # sessions are used in django to be able to remember who 
    #you are  on subsequent visits and store data about your particular session such as ur user id and all of ur tasks
    # sessions are determined by cookies on the different browsers
    if "tasks" not in request.session: # is there already a task in that session?
        request.session["tasks"] = [] # if none, create one
    return render(request, "tasksapp/index.html", {"tasks":request.session["tasks"]}) # pass in that list of task in this particular template

